#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

import base64
import six

def jsonize(data):
    """
    Returns JSON serialized data

    >>> jsonize({'foo':'bar'})
    '{\\n    "foo": "bar"\\n}'
    """

    return json.dumps(data, sort_keys=False, indent=4)

def dejsonize(data):
    """
    Returns JSON deserialized data

    >>> dejsonize('{\\n    "foo": "bar"\\n}') == {u'foo': u'bar'}
    True
    """

    return json.loads(data)
    
def decodeHex(value, binary=True):
    """
    Returns a decoded representation of provided hexadecimal value

    >>> decodeHex("313233") == b"123"
    True
    >>> decodeHex("313233", binary=False) == u"123"
    True
    """

    retVal = value

    if isinstance(value, six.binary_type):
        value = getText(value)

    if value.lower().startswith("0x"):
        value = value[2:]

    try:
        retVal = codecs.decode(value, "hex")
    except LookupError:
        retVal = binascii.unhexlify(value)

    if not binary:
        retVal = getText(retVal)

    return retVal

def encodeHex(value, binary=True):
    """
    Returns a encoded representation of provided string value

    >>> encodeHex(b"123") == b"313233"
    True
    >>> encodeHex("123", binary=False)
    '313233'
    >>> encodeHex(b"123"[0]) == b"31"
    True
    """

    if isinstance(value, int):
        value = six.unichr(value)

    if isinstance(value, six.text_type):
        value = value.encode(UNICODE_ENCODING)

    try:
        retVal = codecs.encode(value, "hex")
    except LookupError:
        retVal = binascii.hexlify(value)

    if not binary:
        retVal = getText(retVal)

    return retVal

def decodeBase64(value, binary=True, encoding=None):
    """
    Returns a decoded representation of provided Base64 value

    >>> decodeBase64("MTIz") == b"123"
    True
    >>> decodeBase64("MTIz", binary=False)
    '123'
    >>> decodeBase64("A-B_CDE") == decodeBase64("A+B/CDE")
    True
    >>> decodeBase64(b"MTIzNA") == b"1234"
    True
    >>> decodeBase64("MTIzNA") == b"1234"
    True
    >>> decodeBase64("MTIzNA==") == b"1234"
    True
    """

    if value is None:
        return None

    padding = b'=' if isinstance(value, bytes) else '='

    # Reference: https://stackoverflow.com/a/49459036
    if not value.endswith(padding):
        value += 3 * padding

    # Reference: https://en.wikipedia.org/wiki/Base64#URL_applications
    # Reference: https://perldoc.perl.org/MIME/Base64.html
    if isinstance(value, bytes):
        value = value.replace(b'-', b'+').replace(b'_', b'/')
    else:
        value = value.replace('-', '+').replace('_', '/')

    retVal = base64.b64decode(value)

    if not binary:
        retVal = getText(retVal, encoding)

    return retVal

def encodeBase64(value, binary=True, encoding=None, padding=True, safe=False):
    """
    Returns a decoded representation of provided Base64 value

    >>> encodeBase64(b"123") == b"MTIz"
    True
    >>> encodeBase64(u"1234", binary=False)
    'MTIzNA=='
    >>> encodeBase64(u"1234", binary=False, padding=False)
    'MTIzNA'
    >>> encodeBase64(decodeBase64("A-B_CDE"), binary=False, safe=True)
    'A-B_CDE'
    """

    if value is None:
        return None

    if isinstance(value, six.text_type):
        value = value.encode(encoding or UNICODE_ENCODING)

    retVal = base64.b64encode(value)

    if not binary:
        retVal = getText(retVal, encoding)

    if safe:
        padding = False

        # Reference: https://en.wikipedia.org/wiki/Base64#URL_applications
        # Reference: https://perldoc.perl.org/MIME/Base64.html
        if isinstance(retVal, bytes):
            retVal = retVal.replace(b'+', b'-').replace(b'/', b'_')
        else:
            retVal = retVal.replace('+', '-').replace('/', '_')

    if not padding:
        retVal = retVal.rstrip(b'=' if isinstance(retVal, bytes) else '=')

    return retVal

def getBytes(value, encoding=None, errors="strict", unsafe=True):
    """
    Returns byte representation of provided Unicode value

    >>> getBytes(u"foo\\\\x01\\\\x83\\\\xffbar") == b"foo\\x01\\x83\\xffbar"
    True
    """

    retVal = value

    if encoding is None:
        encoding = conf.get("encoding") or UNICODE_ENCODING

    try:
        codecs.lookup(encoding)
    except (LookupError, TypeError):
        encoding = UNICODE_ENCODING

    if isinstance(value, six.text_type):
        if INVALID_UNICODE_PRIVATE_AREA:
            if unsafe:
                for char in xrange(0xF0000, 0xF00FF + 1):
                    value = value.replace(_unichr(char), "%s%02x" % (SAFE_HEX_MARKER, char - 0xF0000))

            retVal = value.encode(encoding, errors)

            if unsafe:
                retVal = re.sub(r"%s([0-9a-f]{2})" % SAFE_HEX_MARKER, lambda _: decodeHex(_.group(1)), retVal)
        else:
            try:
                retVal = value.encode(encoding, errors)
            except UnicodeError:
                retVal = value.encode(UNICODE_ENCODING, errors="replace")

            if unsafe:
                retVal = re.sub(b"\\\\x([0-9a-f]{2})", lambda _: decodeHex(_.group(1)), retVal)

    return retVal

def getOrds(value):
    """
    Returns ORD(...) representation of provided string value

    >>> getOrds(u'fo\\xf6bar')
    [102, 111, 246, 98, 97, 114]
    >>> getOrds(b"fo\\xc3\\xb6bar")
    [102, 111, 195, 182, 98, 97, 114]
    """

    return [_ if isinstance(_, int) else ord(_) for _ in value]

def getUnicode(value, encoding=None, noneToNull=False):
    """
    Returns the unicode representation of the supplied value

    >>> getUnicode('test') == u'test'
    True
    >>> getUnicode(1) == u'1'
    True
    >>> getUnicode(None) == 'None'
    True
    """

    if noneToNull and value is None:
        return NULL

    if isinstance(value, six.text_type):
        return value
    elif isinstance(value, six.binary_type):
        # Heuristics (if encoding not explicitly specified)
        candidates = filterNone((encoding, kb.get("pageEncoding") if kb.get("originalPage") else None, conf.get("encoding"), UNICODE_ENCODING, sys.getfilesystemencoding()))
        if all(_ in value for _ in (b'<', b'>')):
            pass
        elif any(_ in value for _ in (b":\\", b'/', b'.')) and b'\n' not in value:
            candidates = filterNone((encoding, sys.getfilesystemencoding(), kb.get("pageEncoding") if kb.get("originalPage") else None, UNICODE_ENCODING, conf.get("encoding")))
        elif conf.get("encoding") and b'\n' not in value:
            candidates = filterNone((encoding, conf.get("encoding"), kb.get("pageEncoding") if kb.get("originalPage") else None, sys.getfilesystemencoding(), UNICODE_ENCODING))

        for candidate in candidates:
            try:
                return six.text_type(value, candidate)
            except (UnicodeDecodeError, LookupError):
                pass

        try:
            return six.text_type(value, encoding or (kb.get("pageEncoding") if kb.get("originalPage") else None) or UNICODE_ENCODING)
        except UnicodeDecodeError:
            return six.text_type(value, UNICODE_ENCODING, errors="reversible")
    elif isListLike(value):
        value = list(getUnicode(_, encoding, noneToNull) for _ in value)
        return value
    else:
        try:
            return six.text_type(value)
        except UnicodeDecodeError:
            return six.text_type(str(value), errors="ignore")  # encoding ignored for non-basestring instances

def getText(value, encoding=None):
    """
    Returns textual value of a given value (Note: not necessary Unicode on Python2)

    >>> getText(b"foobar")
    'foobar'
    >>> isinstance(getText(u"fo\\u2299bar"), six.text_type)
    True
    """

    retVal = value

    if isinstance(value, six.binary_type):
        retVal = getUnicode(value, encoding)

    if six.PY2:
        try:
            retVal = str(retVal)
        except:
            pass

    return retVal

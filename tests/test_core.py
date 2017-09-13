# -*- coding: UTF-8 -*-


"""
Unittests for emoji.core
"""


from __future__ import unicode_literals

import emoji
from nose.tools import assert_raises


def test_emojize_name_only():
    for name in emoji.EMOJI_UNICODE.keys():
        actual = emoji.emojize(name, False)
        expected = emoji.EMOJI_UNICODE[name]
        assert expected == actual, "%s != %s" % (expected, actual)


def test_emojize_complicated_string():
    # A bunch of emoji's with UTF-8 strings to make sure the regex expression is functioning
    name_code = {
        ':flag_for_Ceuta_&_Melilla:': u'\U0001F1EA\U0001F1E6',
        ':flag_for_St._Barthélemy:': u'\U0001F1E7\U0001F1F1',
        ':flag_for_Côte_d’Ivoire:': u'\U0001F1E8\U0001F1EE',
        ':flag_for_Åland_Islands:': u'\U0001F1E6\U0001F1FD',
        ':flag_for_São_Tomé_&_Príncipe:': u'\U0001F1F8\U0001F1F9',
        ':flag_for_Curaçao:': u'\U0001F1E8\U0001F1FC'
    }
    string = ' complicated! '.join(list(name_code.keys()))
    actual = emoji.emojize(string, False)
    expected = string
    for name, code in name_code.items():
        expected = expected.replace(name, code)
    expected = emoji.emojize(actual, False)
    assert expected == actual, "%s != %s" % (expected, actual)


def test_emojize_invalid_emoji():
    string = '__---___--Invalid__--__-Name'
    assert emoji.emojize(string, False) == string


def test_alias():
    # When use_aliases=False aliases should be passed through untouched
    assert emoji.emojize(':soccer:', use_aliases=False) == ':soccer:'
    assert emoji.emojize(':soccer:', use_aliases=True) == emoji.EMOJI_ALIAS_UNICODE[':soccer:']

def test_invalid_alias():
    # Invalid aliases should be passed through untouched
    assert emoji.emojize(':tester:', use_aliases=True) == ':tester:'

def test_demojize_name_only():
    for name in emoji.EMOJI_UNICODE.keys():
        oneway = emoji.emojize(name, False)
        roundtrip = emoji.demojize(oneway)
        assert name == roundtrip, "%s != %s" % (name, roundtrip)

def test_demojize_complicated_string():
    constructed = u"testing :baby::emoji_modifier_fitzpatrick_type-3: with :eyes: :eyes::eyes: modifiers :baby::emoji_modifier_fitzpatrick_type-5: to symbols ヒㇿ"
    emojid = emoji.emojize(constructed)
    destructed = emoji.demojize(emojid)
    assert constructed == destructed, "%s != %s" % (constructed, destructed)

def test_voz_emoji():
    testcases = (
        (':gach:', '<img src="https://vozforums.com/images/smilies/brick.png" id="smilie_265" alt=":gach:" title="Brick">'),
    )

    for src, expected in testcases:
        result = emoji.emojize(src)

        assert result == expected

def test_voz_icon():
    testcases = (
        (':)', '<img src="https://vozforums.com/images/smilies/Off/smile.gif" id="smilie_207" alt=":)" title="Smile">'),
        (':D', '<img src="https://vozforums.com/images/smilies/Off/big_smile.gif" id="smilie_213" alt=":D" title="Big Smile">'),
        (':Denmark:', ':Denmark:'),
        ('^:)^', '<img src="https://vozforums.com/images/smilies/Off/lay.gif" id="smilie_218" alt="^:)^" title="Bow">'),
        (':((', '<img src="https://vozforums.com/images/smilies/Off/cry.gif" id="smilie_197" alt=":((" title="Cry">'),
        (':p', '<img src="https://vozforums.com/images/smilies/tongue.gif" id="smilie_5" alt=":p" title="Stick Out Tongue">'),
        (':puke:', ':puke:'),
        (';)', '<img src="https://vozforums.com/images/smilies/wink.gif" id="smilie_4" alt=";)" title="Wink">'),
        (':-s', '<img src="https://vozforums.com/images/smilies/Off/confuse.gif" id="smilie_217" alt=":-s" title="Confuse">'),
        ('-_-', '<img src="https://vozforums.com/images/smilies/Off/sleep.gif" id="smilie_228" alt="-_-" title="Sleep">'),
        (':">', '<img src="https://vozforums.com/images/smilies/Off/embarrassed.gif" id="smilie_248" alt=":&quot;>" title="Embarrassed">'),
        (':*', '<img src="https://vozforums.com/images/smilies/Off/sweet_kiss.gif" id="smilie_206" alt=":*" title="Sweet Kiss">'),
    )

    for src, expected in testcases:
        result = emoji.iconize(src)

        assert result == expected

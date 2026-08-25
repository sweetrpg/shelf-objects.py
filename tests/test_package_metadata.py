# -*- coding: utf-8 -*-
import sweetrpg_game_room_objects as pkg


def test_package_importable():
    assert pkg.__title__ == "SweetRPG Game Room Objects"


def test_package_has_version():
    assert pkg.__version__

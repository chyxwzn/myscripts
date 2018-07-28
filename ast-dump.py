#!/usr/bin/env python
# -*- coding: utf-8 -*-
import clang.cindex, asciitree, sys

clang.cindex.Config.set_library_file("libclang.so.6")
index = clang.cindex.Index(
    clang.cindex.conf.lib.clang_createIndex(False, True))
# translation_unit = index.parse(sys.argv[1], ['-c'], options=7)
translation_unit = index.read(sys.argv[1])

print(
    asciitree.draw_tree(
        translation_unit.cursor, lambda n: list(n.get_children()),
        lambda n: "%s <line:%d, col:%d> (%s, %s)" % (n.spelling or n.displayname or "unknown", n.location.line, n.location.column, str(n.kind).split(".")[1], str(n.type.kind).split(".")[1]))
    )

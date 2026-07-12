#!/usr/bin/env python3
"""Fix REUSE header in zh_CN.ts after XML processing.

ET.parse/write strips comments and DOCTYPE. Run this after any script
that modifies zh_CN.ts to restore the required SPDX header.

Usage: python tools/fix_ts_header.py
"""

import sys

HEADER = '''<?xml version="1.0" encoding="utf-8"?>
<!-- SPDX-FileCopyrightText: Copyright 2025 shadPS4 Emulator Project
     SPDX-License-Identifier: GPL-2.0-or-later -->
<!DOCTYPE TS>
<TS version="2.1" language="zh_CN" sourcelanguage="en">'''

BROKEN = """<?xml version='1.0' encoding='utf-8'?>
<TS version="2.1" language="zh_CN" sourcelanguage="en">"""

def fix_header(filepath="src/qt_gui/translations/zh_CN.ts"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith(BROKEN):
        content = HEADER + content[len(BROKEN):]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed REUSE header in {filepath}")
        return True
    elif content.startswith(HEADER):
        print(f"Header already correct in {filepath}")
        return False
    else:
        print(f"WARNING: Unexpected file start in {filepath} — manual check needed")
        return False

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else "src/qt_gui/translations/zh_CN.ts"
    fix_header(path)

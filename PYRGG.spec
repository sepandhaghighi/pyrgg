# -*- mode: python -*-

block_cipher = None

pyrgg_version = "1.4"


a = Analysis(['pyrgg/__main__.py'],
             pathex=['pyrgg'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PYRGG-'+pyrgg_version,
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
		  icon='otherfile/icon.ico',
		  version="otherfile/Version.rc",
          console=True )

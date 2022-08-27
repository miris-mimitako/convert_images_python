# convert_images_python

このアプリケーションでは、指定したフォルダ内にある画像ファイルを指定した形式へ変換、圧縮するものです。

This application converts and compresses image files in a specified folder to a specified format.

## setting

セッティング.json のパラメータ指定方法について。

target_dir: 変換対象が保管されているディレクトリを示します。

serch_depth: 変換対象の階層深さを示します。-1 を指定すると配下のディレクトリすべてが変換対象です。

converted_files_dir: 変換後の保存先フォルダを指定します。指定がなければ同じ場所にリネームされたファイルが自動生成されます。

convert_type: 変換後のファイル形式を指定します。

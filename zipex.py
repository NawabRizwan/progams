import zipfile,os

zip = zipfile.ZipFile('newzip.zip','w');
zip.write('aa.txt',compress_type=zipfile.ZIP_DEFLATED)
zip.close()
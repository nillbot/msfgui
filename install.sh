echo "Installing metasploit ..."
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
rm msfinstall

echo "Installing apktool ..."
wget "https://bbuseruploads.s3.amazonaws.com/0becf6a1-1706-4f2e-9ae6-891e00a8dd5f/downloads/fffd0ef9-f07c-4e0c-8f1a-0ed4ee73d12d/apktool_2.9.3.jar?response-content-disposition=attachment%3B%20filename%3D%22apktool_2.9.3.jar%22&AWSAccessKeyId=ASIA6KOSE3BNOML6P4YL&Signature=NyqG5V5yR5802BKiN3YlQH8aoX0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJHMEUCIQDT%2BLAJOT7bDY%2FCHP%2Bz0FRQl5hwUQuCwj2Pz1heoLSE8QIgC%2BA79Gi2Fso2Zl2LT9WPdXa5ZW0wVsFyPWqOchCdcDwqpwIIaRAAGgw5ODQ1MjUxMDExNDYiDPInn5Is%2FImk%2BgSecSqEApQrda%2FrA4ZujlWGxRZzIkcDcTciuQWvnubmEF2j3xFgztQO0cvEsY6K9BDglsxmbgcliNFK0z8VMyBhdxWqOrdOBETogvfO420tEkRbHiGX1RprTsdGJS2KsnjVkwLGGid2wQry9S5oogemWIotuhf91xEIQxl3U0xyAb1S6W%2BcShG%2Ffii1b6vbjWi2PusqxdbsUsvKHyd9zxZNV7WhXXMjgOABgf7kE517oIYJtd8fNIcZXQMDyvxOZu94vhoflwI8o0hHCPBIdF4oGFb%2BKsTj%2FsZNCi%2BsVsVQ5lko3JCnkapkNUe9uDh51My6O2SXaD5l3w2OCW%2F9%2FOGIiomgWToJAnkmMP3X%2Fa8GOp0B5JOZXFSXOkldVz3967l0HQQbiScORgk6wjBpOYBntEdji2QSC7SBhVuhUR051fkvrjdtGhkSqpvwY1YyuUt%2B1%2FxQSX2vybkFrluQlQdYkphkvXvZJcclyXf5tREd88%2F6zXfPSpisgFaX74HrJ1h0zXwtV%2BMyJQ8%2Bqu0KGScb7a3tVr5ticGagtU2m6Q4V9kodKVLgeVWlIwfnV5j7w%3D%3D&Expires=1711239941" -O apktool.jar
wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool
chmod +x *.jar
mv *.jar /usr/local/bin/

echo "Installing apksigner ..."
apt update -y
apt install apksigner -y

echo "Installing zipalign ..."
apt install zipalign -y

echo "Done ..."

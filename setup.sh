mkdir -p ~/.streamlit/
echo "
[general]n
email = "yogesh.singh893@gmail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=truen
port = $PORTn
" > ~/.streamlit/config.toml
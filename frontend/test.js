function httpGetDiscord() 
{
    window.location = "https://discord.com/api/oauth2/authorize?client_id=" + DISCORD_CLIENT_ID + "&redirect_uri=http%3A%2F%2F127.0.0.1%3A5500%2Ffrontend%2Fredirect.html&response_type=code&scope=email"
}
function httpGetGoogle()
{
    window.location = "https://accounts.google.com/o/oauth2/v2/auth?client_id=" + GOOGLE_CLIENT_ID + "&redirect_uri=http://127.0.0.1:5500/frontend/redirect.html&access_type=offline&response_type=code&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
}
using System;
using System.IO;
using System.Net.Http;
string[] users = System.IO.File.ReadAllLines(@"path of the list");
using var client = new HttpClient();
for (int i = 0; i < users.Length; i++)
{
    var result = await client.GetAsync(@"https://www.tiktok.com/@"+users[i]+"?");
    if (result.StatusCode.ToString() == "404")
        Console.WriteLine(users[i]);
}

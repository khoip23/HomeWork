
using System.Text;
using System.Text.Json;
using HomeWork_Day33.ViewModel;

public class ProductService
{
    private HttpClient _httpClient;

    public ProductService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }
     public async Task<List<Store>> GetAllListStore()
    {
        try
        {
            var url = "https://apistore.cybersoft.edu.vn/api/Store/getAll";
            var response = await _httpClient.GetFromJsonAsync<HTTPResponse<List<Store>>>(url);

            if (response != null && response.statusCode == 200)
            {
                return response.content;
            }
            else
            {
                Console.WriteLine("No stores received from API.");
                return new List<Store>();
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error fetching store list: {e.Message}");
            return new List<Store>();
        }
    }


    public async Task<bool> DeleteStore(string id)
    {
        try
        {
            var url = $"https://apistore.cybersoft.edu.vn/api/Store/{id}";

            // Create the HttpRequestMessage with DELETE method
            var request = new HttpRequestMessage
            {
                Method = HttpMethod.Delete,
                RequestUri = new Uri(url)
            };

            // Send the DELETE request asynchronously
            var res = await _httpClient.SendAsync(request);

            // Check if the status code indicates success
            if (res.IsSuccessStatusCode)
            {
                return true;  // Deletion was successful
            }
            else
            {
                Console.WriteLine($"Failed to delete store. Status code: {res.StatusCode}");
                return false; // Deletion failed
            }
        }
        catch (Exception e)
        {
            // Log the exception message if an error occurs
            Console.WriteLine($"Error deleting store: {e.Message}");
            return false; // Error occurred
        }
    }
    public async Task<Store?> GetStoreById(int id)
{
    try
    {
        var url = $"https://apistore.cybersoft.edu.vn/api/Store/getbyid?id={id}";
        var response = await _httpClient.GetFromJsonAsync<HTTPResponse<Store>>(url);
        return response.content;
    }
    catch (Exception e)
    {
        Console.WriteLine($"Error fetching store: {e.Message}");
        return null;
    }
}

public async Task<bool> SaveStore(Store store)
{
        Console.WriteLine($"Saving Store: {JsonSerializer.Serialize(store)}");

    try
    {
        var url = "https://apistore.cybersoft.edu.vn/api/Store";
        var json = JsonSerializer.Serialize(store);
        var content = new StringContent(json, Encoding.UTF8, "application/json-patch+json"); // Sử dụng đúng Content-Type

        HttpResponseMessage response;
        if (store.Id == 0) // Nếu ID = 0 thì tạo mới
        {
            response = await _httpClient.PostAsync(url, content);
        }
        else // Nếu có ID thì update
        {
            url += $"?id={store.Id}"; // Truyền ID qua query
            response = await _httpClient.PutAsync(url, content);
        }

        var responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine($"Response: {response.StatusCode} - {responseText}");

        return response.IsSuccessStatusCode;
    }
    catch (Exception e)
    {
        Console.WriteLine($"Error saving store: {e.Message}");
        return false;
    }
}




}
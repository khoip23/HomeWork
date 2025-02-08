namespace HomeWork_Day33.ViewModel;

using System.Text.Json;



public class Store
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public string? Alias { get; set; }
    public string? Description { get; set; }
    public string? ImageUrl { get; set; }
    public string? Latitude { get; set; }  // Cho phép null
    public string? Longitude { get; set; } // Cho phép null
    public bool IsDeleted { get; set; }

    // Override ToString để in ra JSON
    public override string ToString()
    {
        return JsonSerializer.Serialize(this, new JsonSerializerOptions
        {
            WriteIndented = true // Format JSON đẹp hơn
        });
    }
}


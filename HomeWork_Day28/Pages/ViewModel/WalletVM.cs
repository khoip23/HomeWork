using System.ComponentModel.DataAnnotations;

namespace HomeWork_Day28.ViewModels
{
    public class WalletVM
    {
        public string? Type { get; set; } 
        [Required]
        public double Amount { get; set; } 
        public DateTime Date { get; set; } 
        public double Balance { get; set; } = 111111.11; 


}

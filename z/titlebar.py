import matplotlib.pyplot as plt

# Monthly sales data from January to December
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
sales = [10000, 12000, 9000, 14000, 15000, 13000, 16000, 17000, 14000, 18000, 19000, 20000]

# Create the plot
plt.figure(figsize=(12, 6))

# Plot the data
plt.plot(months, sales, marker='o', linestyle='-', color='#0d6efd', linewidth=2, markersize=8)

# Add titles and labels
plt.title('Monthly Sales Data', fontsize=16, fontweight='bold', color='#333333')
plt.xlabel('Month', fontsize=14, fontweight='bold', color='#333333')
plt.ylabel('Sales (in PHP)', fontsize=14, fontweight='bold', color='#333333')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Customize the ticks
plt.xticks(fontsize=12, fontweight='bold', color='#333333')
plt.yticks(fontsize=12, fontweight='bold', color='#333333')

# Customize the spines
for spine in plt.gca().spines.values():
    spine.set_edgecolor('#333333')

# Display the plot
plt.tight_layout()
plt.show()

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
directory = os.path.join(desktop_path, "allAgetestrun")

# Initialize empty lists to store data from each category
all_hashtags = []
all_authors = []
all_sounds = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        
        # Load data from the file into a DataFrame
        df = pd.read_csv(filepath)
        
        # Extract hashtags, authors, and sounds
        hashtags = df['hashtag'].str.split(',\s*', expand=True).stack()
        authors = df['author']
        sounds = df['music']
        
        # Append data
        all_hashtags.extend(hashtags)
        all_authors.extend(authors)
        all_sounds.extend(sounds)

# Create DataFrames for the three categories
hashtags_df = pd.Series(all_hashtags).value_counts()
authors_df = pd.Series(all_authors).value_counts()
sounds_df = pd.Series(all_sounds).value_counts()

# Keep only the top 15 most frequent items
top_n = 15
top_hashtags = hashtags_df.nlargest(top_n)
top_authors = authors_df.nlargest(top_n)
top_sounds = sounds_df.nlargest(top_n)

# Plot each bar plot individually
plt.figure(figsize=(15, 12))

# Plot Top Hashtags
plt.subplot(3, 1, 1)
sns.barplot(x=top_hashtags.values, y=top_hashtags.index, palette="Blues_d")
for i, value in enumerate(top_hashtags.values):
    plt.text(value, i, f'{value}', va='center')
plt.title('Cumulative Top Hashtags_', fontweight='bold')
plt.xlabel('Frequency')
plt.ylabel('Hashtag')

# Plot Top Authors
plt.subplot(3, 1, 2)
sns.barplot(x=top_authors.values, y=top_authors.index, palette="Greens_d")
for i, value in enumerate(top_authors.values):
    plt.text(value, i, f'{value}', va='center')
plt.title('Cumulative Top Content Creators', fontweight='bold')
plt.xlabel('Frequency')
plt.ylabel('Content Creator')

# Plot Top Sounds
plt.subplot(3, 1, 3)
sns.barplot(x=top_sounds.values, y=top_sounds.index, palette="Oranges_d")
for i, value in enumerate(top_sounds.values):
    plt.text(value, i, f'{value}', va='center')
plt.title('Cumulative Top Audio', fontweight='bold')
plt.xlabel('Frequency')
plt.ylabel('Audio')

plt.tight_layout()
plt.show()

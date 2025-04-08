import pandas as pd

def downsample_csv(input_csv, output_csv, total_samples):
    # Load the dataset
    df = pd.read_csv(input_csv)

    # Separate by class
    phishing_df = df[df['label'] == 1]
    legit_df = df[df['label'] == 0]

    # Calculate how many samples per class (ensure balance)
    samples_per_class = total_samples // 2

    # Downsample each class
    phishing_downsampled = phishing_df.sample(n=samples_per_class, random_state=42)
    legit_downsampled = legit_df.sample(n=samples_per_class, random_state=42)

    # Combine and shuffle
    downsampled_df = pd.concat([phishing_downsampled, legit_downsampled]).sample(frac=1, random_state=42)

    # Save to new CSV
    downsampled_df.to_csv(output_csv, index=False)
    print(f"saved to {output_csv}")

# Example usage
downsample_csv(r"input path", r"outputpath", total_samples=480000)

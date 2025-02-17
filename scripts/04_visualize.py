import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed data
df = pd.read_csv("data/processed_sleep_data.csv")

# Sleep Duration vs. Stress Level
plt.figure()
sns.scatterplot(x=df['Sleep Duration'], y=df['Stress Level'])
plt.title('Sleep Duration vs. Stress Level')
plt.savefig("outputs/sleep_stress.png")

# Sleep Disorder distribution across BMI
plt.figure()
sns.countplot(x=df['BMI Category'], hue=df['Sleep Disorder'])
plt.title('BMI Category vs. Sleep Disorder')
plt.savefig("outputs/bmi_sleep_disorder.png")

# Physical Activity vs. Quality of Sleep
plt.figure()
sns.boxplot(x=df['Quality of Sleep'], y=df['Physical Activity Level'])
plt.title('Physical Activity Level and Sleep Quality')
plt.savefig("outputs/activity_sleep_quality.png")

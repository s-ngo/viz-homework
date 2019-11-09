import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/housing.data',
                 sep='\s+',
                 header=0)

# Setting columns to dataset
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

os.makedirs('plots/data_exploration', exist_ok=True)

# # Another useful dataset exploration technique involves comparing multiple columns of the dataset
# # The enumerate functions will generate pairs of indexes elements
# for col1_idx, column1 in enumerate(df.columns):
#     for col2_idx, column2 in enumerate(df.columns):
#         if col1_idx < col2_idx:
#             print(f'Generating {column1} to {column2} plot')
#             fig, axes = plt.subplots(1, 1, figsize=(5, 5))
#             axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='red', marker='1')
#             axes.set_title(f'{column1} to {column2}')
#             axes.set_xlabel(column1)
#             axes.set_ylabel(column2)
#             axes.legend()
#             plt.savefig(f'plots/data_exploration/housing_{column1}_{column2}_scatter.png', dpi=300)
#             plt.close(fig)
# plt.close()

# # Generating a heatmap
# sns.set()
#
# fig, ax = plt.subplots(figsize=(12,12))
# sns.heatmap(df.corr(), annot=True, cmap='autumn')
# ax.set_xticklabels(df.columns, rotation=45)
# ax.set_yticklabels(df.columns, rotation=45)
# plt.savefig('plots/data_exploration/boston_heatmap.png')
#
# plt.close()


# # Loop to print a ton of multiplots to check MEDV
# for col1_indx, column1 in enumerate(df.columns):
#     for col2_indx, column2 in enumerate(df.columns):
#         for col3_indx, column3 in enumerate(df.columns):
#             if col1_indx < col2_indx and col2_indx < col3_indx:
#                 plt.style.use("ggplot")
#                 fig, axes = plt.subplots(1, 1, figsize=(5, 5))
#                 # This time we plot multiple plots on the same axes, to get some perspective on their comparisons
#                 axes.scatter(df['MEDV'], df[column1], alpha=0.7, label=f'{column1}')
#                 axes.scatter(df['MEDV'], df[column2], alpha=0.7, label=f'{column2}')
#                 axes.scatter(df['MEDV'], df[column3], alpha=0.7, label=f'{column3}')
#
#                 axes.set_xlabel('MEDV')
#                 axes.set_ylabel(f'{column1}/{column2}/{column3}')
#                 axes.set_title(f'MEDV compared to {column1}/{column2}/{column3}')
#                 axes.legend()
#                 plt.savefig(f'plots/multiplot_MEDV_{column1}_{column2}_{column3}_scatter.png', dpi=300)
#                 plt.close(fig)
# plt.close()

# Loop to print a ton of multiplots to check RM
for col1_indx, column1 in enumerate(df.columns):
    for col2_indx, column2 in enumerate(df.columns):
        for col3_indx, column3 in enumerate(df.columns):
            if col1_indx < col2_indx and col2_indx < col3_indx:
                plt.style.use("ggplot")
                fig, axes = plt.subplots(1, 1, figsize=(5, 5))
                # This time we plot multiple plots on the same axes, to get some perspective on their comparisons
                axes.scatter(df['RM'], df[column1], alpha=0.7, label=f'{column1}')
                axes.scatter(df['RM'], df[column2], alpha=0.7, label=f'{column2}')
                axes.scatter(df['RM'], df[column3], alpha=0.7, label=f'{column3}')

                axes.set_xlabel('RM')
                axes.set_ylabel(f'{column1}/{column2}/{column3}')
                axes.set_title(f'RM compared to {column1}/{column2}/{column3}')
                axes.legend()
                plt.savefig(f'plots/multiplot_RM_{column1}_{column2}_{column3}_scatter.png', dpi=300)
                plt.close(fig)
plt.close()
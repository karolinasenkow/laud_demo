library(pheatmap)
library(dplyr)
library(ggplot2)

df <- read.csv("laud/dim_df.csv")

df_subset = as.matrix(df[, 3:ncol(df)])

rownames(df_subset) = sapply(df$sample_id, function(x) 
  strsplit(as.character(x),split = "\\\\")[[1]][1])

x <- names(sort(colMeans(df_subset), decreasing = T)[1:30])

df_subset <- df_subset[,x]

cure_df = data.frame("cure_status" = df$cure_status)
rownames(cure_df) = rownames(df_subset) # name matching

y <- names(sort(rowMeans(df_subset), decreasing = T)[1:50])

df_subset <- df_subset[y,]

cure_df <- as.data.frame(cure_df[y,])
rownames(cure_df) = rownames(df_subset) # name matching
cure_df <- cure_df %>%
  rename(cure_status = `cure_df[y, ]`)



pheatmap(df_subset, scale = "row", annotation_row = cure_df)

ggsave("laud/static/images/graphs/two_hierch.png")



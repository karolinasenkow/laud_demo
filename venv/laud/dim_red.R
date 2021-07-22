#!/usr/bin/Rscript
args = commandArgs(trailingOnly = TRUE)

library(ggplot2)
library(ggfortify)
library(Rtsne)
library(ggforce)

setwd(getwd())
set.seed(42)

vec <- read.csv("laud/static/uploads/ML_sample_input.csv")
vec <- cbind(cure_status = "unkown", vec)

df <- read.csv("laud/dim_df.csv")
data <- rbind(vec, df)
data1 <- data[,3:ncol(data)] #species
cure_status <- data[,1] #cure status


if (args[1] == "tsne") {
  tsne <- Rtsne(data1, perplexity= 1,  check_duplicates = FALSE)
  tsne_plot <- data.frame(x = tsne$Y[,1], y = tsne$Y[,2], cure_status = cure_status)
  ggplot(tsne_plot, aes(x=x, y=y, color=cure_status)) + 
    geom_point() + 
    stat_ellipse(type = "norm", linetype = 2) +  
    geom_mark_ellipse(aes(fill = cure_status, color = cure_status))
  ggsave("laud/static/images/graphs/dim_red.png")
} else {
  pca <- prcomp(data1, center = TRUE, rank = 10) 
  df_out <- as.data.frame(pca$x)
  theme_set(theme_bw())
  ggplot(df_out, aes(x = PC1, y = PC2, color = cure_status)) + 
	  geom_point() + 
	  stat_ellipse(type = "norm", linetype = 2)+
	  geom_mark_ellipse(aes(fill = cure_status, color = cure_status))
  ggsave("laud/static/images/graphs/dim_red.png")
}


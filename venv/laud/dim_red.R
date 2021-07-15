#!/usr/bin/Rscript
args = commandArgs(trailingOnly = TRUE)

library(ggplot2)
library(ggfortify)
library(Rtsne)

setwd(getwd())
set.seed(42)
data <- read.csv("laud/dim_red_df.csv")
data1 <- log(data[,3:ncol(data)]) #species
cure_status <- data[,1] #cure status


if (args[1] = "tsne") {
  tsne <- Rtsne(data1, perplexity = 30, check_duplicates = FALSE)
  tsne_plot <- data.frame(x = tsne$Y[,1], y = tsne$Y[,2], cure_status = cure_status)
  ggplot(tsne_plot, aes(x=x, y=y, color=cure_status)) + 
    geom_point() + 
    stat_ellipse(type = "norm")
  ggsave("laud/static/images/graphs/dim_red.png")
} else {
  pca <- prcomp(data1, center = TRUE, scale. = TRUE, rank = 10) #standardizes the data
  summary(pca)
  theme_set(theme_bw())
  autoplot(pca, data = data, loadings = TRUE, loadings.label = TRUE, colour = "cure_status", frame = TRUE, frame.type="norm")
  ggsave("laud/static/images/graphs/dim_red.png")
}

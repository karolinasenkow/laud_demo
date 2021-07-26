library(ggplot2)

path = getwd()
full_path <- paste(path, "laud", "t_test_df.csv", sep="/")
data <- read.csv(file = full_path, header=TRUE)
attach(data)

# Start writing to an output file
output <- paste(path, 'laud', 'analysis-output.txt', sep="/")
t_test_boxplot <- paste(path, 'laud', 'static', 'images', 'graphs', 'boxplot.png', sep="/")

# 1. Open jpeg file
png(t_test_boxplot)
# 2. Create the plot
#boxplot(taxa_count~cure_status)
ggplot(data, aes(x = cure_status, y = taxa_count, color = cure_status)) +
	geom_boxplot() + 
	theme_bw() +
        theme(text = element_text(size = 15))	
# 3. Close the file
dev.off()

uni <- unique(data[c("cure_status")])[,1]
vector = vector()
for (i in 1:length(uni)) {
	cat <- subset(data, cure_status == uni[i])
	num = nrow(cat)
	vector[i] <- num
}

bool <- vector < 25

sink(output)

if (length(which(bool)) == 0) {
	t.test(taxa_count ~ cure_status, mu = 0, alt = "two.sided", conf = 0.95, var.eq = F, paired = F)
} else {
	wilcox.test(taxa_count ~ cure_status, mu = 0, alt = "two.sided", conf = 0.95, paired = F)
}

sink()

#sink(output)

#t.test(taxa_count~cure_status, mu=0, alt="two.sided", conf=0.95, var.eq=F, paired=F)

#sink()

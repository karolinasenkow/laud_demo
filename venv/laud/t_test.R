path = getwd()
full_path <- paste(path, "laud", "t_test_df.csv", sep="/")
data <- read.csv(file = full_path, header=TRUE)
attach(data)

# Start writing to an output file
output <- paste(path, 'laud', 'analysis-output.txt', sep="/")
t_test_boxplot <- paste(path, 'laud', 'templates', 'boxplot.png', sep="/")

# 1. Open jpeg file
png(t_test_boxplot)
# 2. Create the plot
boxplot(taxa_count~cure_status)
# 3. Close the file
dev.off()

sink(output)

t.test(taxa_count~cure_status, mu=0, alt="two.sided", conf=0.95, var.eq=F, paired=F)

sink()

clear all

total_btc_node = 9754;
y = [0.2 0.5 1.0 1.0 1.0 1.5 1.5 3.4 4.9 6.8 8.3 9.0 10.0 10.3 10.5 13.7 15.4];
hash_dist = [100-sum(y) y];
res_btc_node = total_btc_node - length(hash_dist);

x = zeros(1, length(hash_dist));
x(1) = res_btc_node / total_btc_node;
for i = 2:length(hash_dist)
    x(i) = 18/17/total_btc_node;
end


past = (0);
current = 0;
area = 0;
iter = 1;
for i = 1:length(hash_dist)
    hash_dist(i) = hash_dist(i) / 100;
    current = hash_dist(i) + past(i);
    area = area + (past(i)+current)*x(iter)/2;
    past(i+1) = current;
    iter = iter + 1;
end

result = 1 - 2*(1/2 - area);
x_sum = (0);
for i = 1:length(hash_dist)
    x_sum(i+1) = x_sum(i) + x(i);
end
plot(x_sum, past)
hold on
plot([0 1], [0 1])
legend('Lorenz curve', 'Line of equality', 'Location','northwest', 'FontSize',20)








total_eth_node = 11034;
y = [1 1 1 1 2 3 3 4 4 4 8 10 10 13 13 21];
hash_dist = [100-sum(y) y];
res_eth_node = total_eth_node - length(hash_dist);

x = zeros(1, length(hash_dist));
x(1) = res_eth_node / total_eth_node;
for i = 2:length(hash_dist)
    x(i) = 17/16/total_eth_node;
end


past = (0);
current = 0;
area = 0;
iter = 1;
for i = 1:length(hash_dist)
    hash_dist(i) = hash_dist(i) / 100;
    current = hash_dist(i) + past(i);
    area = area + (past(i)+current)*x(iter)/2;
    past(i+1) = current;
    iter = iter + 1;
end

result = 1 - 2*(1/2 - area);
x_sum = (0);
for i = 1:length(hash_dist)
    x_sum(i+1) = x_sum(i) + x(i);
end
plot(x_sum, past)
hold on
plot([0 1], [0 1])
legend('Lorenz curve', 'Line of equality', 'Location','northwest', 'FontSize',20)


% plot(x_sum(3:18), past(3:18))
% lgd = legend('Lorenz curve', 'Location','northwest', 'FontSize',20);

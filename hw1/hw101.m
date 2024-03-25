x = linspace(0.93, 0.97, 10000);
y = x .* sin((x - 2) ./ (x - 1));
plot(x, y, 'LineWidth', 2);
grid on;

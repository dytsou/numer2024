p0 = [0, 0];
p1 = [1, 0.3];
p1n = [1, 1.15];
p2 = [2, 1.7];
p2n = [2, 3.4];
p3 = [3, 1.5];

figure;
hold on;
x = linspace(0, 3, 3000);
f = -2.7*((x/3).^3) + 3.3*((x/3).^2) + 0.9*(x/3);
f2 = -12.15*((x/3).^3) + 17.1*((x/3).^2) + -3.45*(x/3);
plot(x, f, 'b', 'LineWidth', 2);
plot(x, f2, 'g', 'LineWidth', 2);
plot(p0(1), p0(2), 'ro', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
plot(p1(1), p1(2), 'ro', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
plot(p1n(1), p1n(2), 'rx', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
plot(p2(1), p2(2), 'ro', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
plot(p2n(1), p2n(2), 'rx', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
plot(p3(1), p3(2), 'ro', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
plot([p0(1), p1(1)], [p0(2), p1(2)], 'r--', 'LineWidth', 1);
plot([p1(1), p2(1)], [p1(2), p2(2)], 'r--', 'LineWidth', 1);
plot([p2(1), p3(1)], [p2(2), p3(2)], 'r--', 'LineWidth', 1);
grid on;
hold off;



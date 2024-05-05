x0 = linspace(-1, -0.5, 500);
x1 = linspace(-0.5, 0, 500);
x2 = linspace(0, 0.5, 500);
x3 = linspace(0.5, 1, 500);

f00 = zeros(1, 500);
f01 = 1 - 2*abs(x1);
f02 = 1 - 2*abs(x2);
f03 = zeros(1, 500);

f10 = -4*((x0+1).^2)+2*(x0+1);
f11 = -8*((x1+0.5).^3) +4*((x1+0.5).^2)+ 2*(x1+0.5);
f12 = 8*(x2.^3)- 8*(x2.^2)+1;
f13 = -4*(x3-0.5).^2+2*(x3-0.5);

f20 = (x0+1).^2-0.5*(x0+1);
f21 = -5*((x1+0.5).^3) +(x1+0.5).^2+2.75*(x1+0.5);
f22 = 5*(x2.^3)-6.5*(x2.^2)+1;
f23 = (x3-0.5).^2-0.5*(x3-0.5);

figure;
hold on;
plot(x0, f00, 'r--', 'LineWidth', 2);
plot(x0, f10, 'b', 'LineWidth', 1);
plot(x0, f20, 'g', 'LineWidth', 1);

plot(x1, f01, 'r--', 'LineWidth', 2);
plot(x1, f11, 'b', 'LineWidth', 1);
plot(x1, f21, 'g', 'LineWidth', 1);

plot(x2, f02, 'r--', 'LineWidth', 2);
plot(x2, f12, 'b', 'LineWidth', 1);
plot(x2, f22, 'g', 'LineWidth', 1);

plot(x3, f03, 'r--', 'LineWidth', 2);
plot(x3, f13, 'b', 'LineWidth', 1);
plot(x3, f23, 'g', 'LineWidth', 1);
legend('f(x)', 'condition 3', 'condition 4');

grid on;
hold off;
% x = linspace(-pi, pi, 1000);
x = linspace(-1, 1, 11);
f = cos(x);
f1 = 1-x.^2/2+x.^4/24;
f2 = 1-0.49996*x.^2+0.0416*x.^4;

for i = 1:11
    f1x = f1(i)-f(i);
    f2x = f2(i)-f(i);
    disp(x(i));
    disp(f(i));
    disp(f1(i));
    disp(f1x);
    disp(f2(i));
    disp(f2x);
end

figure;
hold on;
plot(x, f, 'r', 'LineWidth', 2);
plot(x, f1, 'b--', 'LineWidth', 1);
plot(x, f2, 'g--', 'LineWidth', 1);
legend('f(x)', 'Power Series', 'Chebyshev Series');
grid on;
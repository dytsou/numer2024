x = linspace(-5, 5, 1000); 
x_pos = linspace(0, 5, 1000); 
x_neg = linspace(-5, 0, 1000);

% Define the functions
f1 = x;
f2_pos = sqrt(exp(x_pos)/2);
f2_neg = -sqrt(exp(x_neg)/2);

% Plot both functions
figure;
hold on; % This keeps the current graph and adds the new plots to it
plot(x, f1, 'r--', 'LineWidth', 2); 
plot(x_pos, f2_pos, 'b', 'LineWidth', 2); 
plot(x_neg, f2_neg, 'b', 'LineWidth', 2); 
plot(xlim, [0 0], 'k--'); 
grid on;
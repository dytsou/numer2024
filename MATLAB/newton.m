function x1 = newton(f, df, x0, tol);
    while abs(f(x0)) > tol,
    x1 = x0 - f(x0)/df(x0);
    h0 = text(x0, f(x0), 'x0');
    h1 = text(x1, f(x1), 'x1');
    pause;
    delete(h0);
    delete(h1);
    disp(x0);
    x0 = x1;
    end;
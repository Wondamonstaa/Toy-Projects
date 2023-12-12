function BinomialNormal(n, p)

close all
b = zeros(1, n+1);
for x = 0:n
    b(x+1) = binopdf(x,n,p);
end

bar(0:n,b);
axis([-1/2 n+1/2 0 max(b)*1.05]);
mu = n*p;
sigma = sqrt(n*p*(1-p));

z = (p - 1/2 - mu)/sigma;
row = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
col = [-3.4, -3.3, -3.2, -3.1, -3.0, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -0.0];
%Int = trapz(row, -1./col);

disp(['mean = ', num2str(mu), ', var. = ', num2str(sigma^2), ', std. dev. = ', num2str(sigma), ', and P(X < 4.5) = ', num2str(z)])
set(gca, 'FontSize', 18)
xlabel('x', 'FontSize', 24)
ylabel('f(x)', 'FontSize', 24)
zlabel('z', 'FontSize', 24)
title(['b(x;', num2str(n), ',', num2str(p), ', z: ', num2str(z), ')'], 'FontSize', 36)

hold on 
xs = -n:n/1000:2*n;
fs = 1/sqrt(2*pi)/sigma * exp((-(xs-mu).^2)/2/sigma^2);
z = (p - 1/2 - mu)/sigma;

%plot(Int);
defects = z:n;

y = binopdf(defects, n, p);
%plot(defects, y);


plot(xs, fs, 'LineWidth', 3)
%plot(z, 'LineWidth', 3)



end 

def filterdesign_tf_coeffs(fs = 1000, n = 1000):
  # % Bookkeeping
  #     f = np.linspace(0,fs/2-1,n/2);   %Define positive frequencies
  #     H = ones(1,n/2);            %Preallocate memory for transfer function
  # % Define Single-Sided DFT  according to specification
  #     H((1*n/fs):(20*n/fs)) = 0;
  #     H((20*n/fs):(50*n/fs)) = -0.5 + 0.03*f((20*n/fs):(50*n/fs));
  #     H((50*n/fs):(250*n/fs)) = 1;
  #     H((250*n/fs):(2250*n/fs)) = 1.125-0.0005*f((250*n/fs):(2250*n/fs));
  #     H((2250*n/fs):(n/2)) = 0;
  # % Convert Single-Sided DFT to Double-Sided
  #     H = [H, flip(H)];
  # % Add a constant phase delay to produce a group delay of 250 samples
  # % This will produce an FIR filter with an order of 500
  #     H = H.*exp(-1i*2*pi/n*250*(0:n-1));
  # % Compute time-domain representation for our filter
  #     h = ifft(H);
  # % Define FIR filter numerator coefficients
  #     b = h(1:500);
  print("Goodbye, World!")

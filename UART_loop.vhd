library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity UART_loop is
	port(
		clk_i: in std_logic;
		rst_i: in std_logic;
		uart_rxd_i: in std_logic;
		uart_txd_o: out std_logic;
		leds  : out std_logic_vector(2-1 downto 0);
		rgb_1  : out std_logic_vector(3-1 downto 0);
		rgb_2  : out std_logic_vector(3-1 downto 0);
		empty_o: out std_logic;
		switch : in std_logic;
		full_o: out std_logic
	);
end;

architecture UART_loop_arq of UART_loop is

	signal w_data_signal, r_dataSignal: std_logic_vector(7 downto 0);
	signal rd_uart_signal, wr_uart_signal: std_logic;
	signal emptySignal,switch_s: std_logic;
	signal led_s : std_logic_vector(2-1 downto 0);
	signal led_rgb_1 : std_logic_vector(3-1 downto 0);
	signal led_rgb_2 : std_logic_vector(3-1 downto 0);
	
	component uart_control is
	port(
		clk_i: in std_logic;
		empty_o: in std_logic;
		rd_uart: out std_logic;
		wr_uart: out std_logic
	);
    end component;
    
    component sistema is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		switch : in std_logic;
		leds : out std_logic_vector(2-1 downto 0);
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;

begin
	
	
	
	uart_inst: entity work.uart
		generic map(
			DVSR		=> 407,	-- baud rate divisor
								-- DVSR = 100M / (16 * baud rate)
								-- baud rate = 19200
			DVSR_BIT	=> 9, 	-- # bits of DVSR
			FIFO_W		=> 6 	-- # addr bits of FIFO
								-- # words in FIFO=2^FIFO_W			
		)
		port map(
			clk 		=> clk_i,
			reset 		=> rst_i,
			rd_uart 	=> rd_uart_signal,
			wr_uart 	=> wr_uart_signal,
			rx 			=> uart_rxd_i,
			w_data 		=> w_data_signal,
			tx_full 	=> full_o,
			rx_empty	=> emptySignal,
			r_data  	=> r_dataSignal,
			tx  		=> uart_txd_o	   
		);
	
	uart_ctrl: uart_control
		port map(
			clk_i 		=>  clk_i,
			empty_o     =>  emptySignal,
			rd_uart     => rd_uart_signal,
			wr_uart     => wr_uart_signal
		);	
	
	
	sistema_i: sistema
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			r_data      => r_dataSignal,
			switch      => switch,
			leds        => led_s,
			led_rgb_1   => led_rgb_1,
			led_rgb_2   => led_rgb_2,
			w_data      => w_data_signal
		);	
		
	empty_o <= emptySignal;
	
	rgb_1       <= led_rgb_1;
	rgb_2       <= led_rgb_2;
	leds       <= led_s;

end;
	
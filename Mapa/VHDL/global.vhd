-- global.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
	entity global is
		port(
			Clock :  in std_logic;
			uart_rxd_i :  in std_logic;
			uart_txd_o :  out std_logic;
			leds :  out std_logic_vector(4-1 downto 0);
			rgb_1 :  out std_logic_vector(3-1 downto 0);
			rgb_2 :  out std_logic_vector(3-1 downto 0);
			switch1 :  in std_logic;
			switch2 :  in std_logic;
			Reset :  in std_logic
		);
	end entity global;
architecture Behavioral of global is
	component uart_control is
		port(
			Clock :  in std_logic;
			N :  out integer;
			escribir :  in std_logic;
			vacio_in :  in std_logic;
			rd_uart :  out std_logic;
			wr_uart :  out std_logic;
			Reset :  in std_logic
		);
	end component uart_control;
	component sistema is
		port(
			Clock :  in std_logic;
			reset_uart :  out std_logic;
			r_disponible :  in std_logic;
			leer :  out std_logic;
			escribir :  out std_logic;
			r_data :  in std_logic_vector(8-1 downto 0);
			switch1 :  in std_logic;
			switch2 :  in std_logic;
			N :  in integer;
			leds :  out std_logic_vector(4-1 downto 0);
			led_rgb_1 :  out std_logic_vector(3-1 downto 0);
			led_rgb_2 :  out std_logic_vector(3-1 downto 0);
			w_data :  out std_logic_vector(8-1 downto 0);
			Reset :  in std_logic
		);
	end component sistema;
	Signal w_data_signal, r_dataSignal: std_logic_vector(7 downto 0);
	Signal rd_uart_signal, wr_uart_signal: std_logic;
	Signal emptySignal,empty_s,tx_empty_s,switch_s,reset_s,reset_uart: std_logic;
	Signal led_s : std_logic_vector(4-1 downto 0);
	Signal led_rgb_1,led_rgb_2 : std_logic_vector(3-1 downto 0);
	Signal N_s : integer;
	Signal leer_s,escribir_s : std_logic;
begin
	uart_inst : entity work.uart
		generic map(
			DVSR      => 407,	-- baud rate divisor DVSR = 125M / (16 * baud rate) baud rate = 19200
			DVSR_BIT  => 9,   --  bits of DVSR
			FIFO_W_RX	=> 6, 	--  addr bits of FIFO words in FIFO=2^FIFO_W 
			FIFO_W_TX	=> 5 	--  addr bits of FIFO words in FIFO=2^FIFO_W 
		)
		port map(
			clk 		=> Clock,
			reset 		=> Reset,
			rd_uart 	=> rd_uart_signal,
			wr_uart 	=> wr_uart_signal,
			rx 			=> uart_rxd_i,
			w_data 		=> w_data_signal,
			rx_empty	=> emptySignal,
			r_data  	=> r_dataSignal,
			tx  		=> uart_txd_o
		);
	uart_control_i : uart_control
		port map(
			Clock => Clock,
			Reset => reset_uart,
			N => N_s,
			escribir => escribir_s,
			vacio_in => emptySignal,
			rd_uart => rd_uart_signal,
			wr_uart => wr_uart_signal
		);
	sistema_i : sistema
		port map(
			Clock => Clock,
			Reset => Reset,
			reset_uart => reset_s,
			r_disponible => rd_uart_signal,
			leer => leer_s,
			escribir => escribir_s,
			r_data => r_dataSignal,
			switch1 => switch1,
			switch2 => switch2,
			N => N_s,
			leds => led_s,
			led_rgb_1 => led_rgb_1,
			led_rgb_2 => led_rgb_2,
			w_data => w_data_signal
		);
	rgb_1 <= led_rgb_1;
	rgb_2 <= led_rgb_2;
	leds <= led_s;
	reset_uart <= Reset or reset_s;
end Behavioral;
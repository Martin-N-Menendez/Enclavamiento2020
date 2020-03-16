-- uart.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
	entity uart is
		generic(
			-- 19200 baud, 8 data bits, 1 stop bit, 2^2 FIFO
			DBIT: integer := 8; -- # data bits
			SB_TICK: integer := 16;	-- # ticks for stop bits, 16/24/32 -- for 1/1.5/2 stop bits
			DVSR: integer := 407; 	-- baud rate divisor -- DVSR = 125M / (16 * baud rate)
			DVSR_BIT: integer := 9; 	-- # bits of DVSR
			FIFO_W_TX: integer := 4; 	-- # addr bits of FIFO_TX # words in FIFO=2^FIFO_W
			FIFO_W_RX: integer := 4 	-- # addr bits of FIFO_TX # words in FIFO=2^FIFO_W
		);
		port(
			clk, reset : in std_logic;
			rd_uart, wr_uart : in std_logic;
			rx : in std_logic;
			w_data : in std_logic_vector(8-1 downto 0);
			tx_full, rx_empty : out std_logic;
			r_data : out std_logic_vector(8-1 downto 0) ;
			tx : out std_logic
		);
	end entity uart;
architecture Behavioral of uart is
	signal rx_done_tick : std_logic;
	signal tick : std_logic;
	signal tx_fifo_out : std_logic_vector(8-1 downto 0);
	signal rx_data_out : std_logic_vector(8-1 downto 0);
	signal tx_empty, tx_fifo_not_empty : std_logic;
	signal tx_done_tick : std_logic;
begin
	baud_gen_unit: entity work.uart_baud_gen(arch)
		generic map(M => DVSR, N => DVSR_BIT)
		port map(clk => clk, reset => reset,
				q => open, max_tick => tick);
	uart_rx_unit: entity work.uart_rx(arch)
		generic map(DBIT=>DBIT, SB_TICK=>SB_TICK)
		port map(clk=>clk, reset=>reset, rx=>rx,
				s_tick=>tick, rx_done_tick=>rx_done_tick,
				d_out => rx_data_out);
	fifo_rx_unit: entity work.fifo(arch)
		generic map(B => DBIT, W => FIFO_W_RX)
		port map(clk => clk, reset => reset, rd => rd_uart,
				wr => rx_done_tick, w_data => rx_data_out,
				empty => rx_empty, full => open, r_data => r_data);
	fifo_tx_unit: entity work.fifo(arch)
		generic map(B => DBIT, W => FIFO_W_TX)
		port map(clk => clk, reset => reset, rd => tx_done_tick,
				wr=>wr_uart, w_data=>w_data, empty => tx_empty,
				full=>tx_full, r_data=>tx_fifo_out);
	uart_tx_unit: entity work.uart_tx(arch)
		generic map(DBIT=>DBIT, SB_TICK=>SB_TICK)
		port map(clk=>clk, reset=>reset,
				tx_start => tx_fifo_not_empty,
				s_tick => tick, d_in => tx_fifo_out,
				tx_done_tick => tx_done_tick, tx => tx);
	tx_fifo_not_empty <= not tx_empty;
end Behavioral;
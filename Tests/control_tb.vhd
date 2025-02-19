-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_control is
end tb_control;

architecture tb of tb_control is

    component uart_control is
	port(
		clk_i: in std_logic;
        	rst_i: in std_logic;
        	leer : in std_logic;
       	 	escribir : in std_logic;
       	 	N : out integer;
		empty_o: in std_logic;
		full_o: in std_logic;
		rd_uart: out std_logic;
		wr_uart: out std_logic
	);
    end component;

    signal clk_i     : std_logic;
    signal rst_i     : std_logic;
    signal leer     : std_logic;
    signal escribir     : std_logic;
    signal N : integer;
    signal empty_o   : std_logic; 
    signal full_o    : std_logic;
    signal rd_uart    : std_logic;
    signal wr_uart    : std_logic;

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : uart_control
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              leer   => leer,
              escribir => escribir,
	      N   => N,
              empty_o => empty_o,
	      full_o   => full_o,
              rd_uart => rd_uart,
              wr_uart     => wr_uart);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk_i is really your main clock signal
    clk_i <= TbClock;

    
	
--    stimuli : process
--    begin
--        -- EDIT Adapt initialization as needed
--        --r_data <= (others => '0');
--
--        -- Reset generation
--        -- EDIT: Check that rst_i is really your reset signal
--        rst_i <= '1';
--        wait for 20 ns;
--        rst_i <= '0';
--	wait for 1 ns;
--	
--        wait for 1000000 * TbPeriod;
--
--        -- Stop the clock and hence terminate the simulation
--        --TbSimEnded <= '1';
--        --wait;
--    end process;

    datos : process
    begin
        rst_i <= '0';
        full_o <= '1';
	leer <= '0';
	escribir <= '0';

        empty_o <= '0';
 	wait for 10 * TbPeriod;
	empty_o <= '1';
	wait for 1 * TbPeriod;
	rst_i <= '1';
 	wait for 1 * TbPeriod;
	
	rst_i <= '0';
	empty_o <= '0';
 	wait for 5 * TbPeriod;
	empty_o <= '1';
	wait for 1 * TbPeriod;
	rst_i <= '1';
 	wait for 1 * TbPeriod;

        --wait for 100 * TbPeriod;
	--TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_control of tb_control is
    for tb
    end for;
end cfg_tb_control;
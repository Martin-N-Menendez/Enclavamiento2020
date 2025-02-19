-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_fifo_enclavamiento is
end tb_fifo_enclavamiento;

architecture tb of tb_fifo_enclavamiento is

    component fifo_enclavamiento is
	port(
		clk_i: in std_logic;
        	rst_i: in std_logic;
		paquete_ok : in std_logic;
        	paquete_i: in std_logic_vector(15-1 downto 0);
        	w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;

    signal clk_i     : std_logic;
    signal rst_i     : std_logic;
    signal paquete_ok     : std_logic;
    signal paquete_i   : std_logic_vector (15-1 downto 0); 
    signal w_data    : std_logic_vector (8-1 downto 0);

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : fifo_enclavamiento
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              paquete_i   => paquete_i,
              paquete_ok => paquete_ok,
              w_data     => w_data);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk_i is really your main clock signal
    clk_i <= TbClock;

    paquete_i <= "101010101010101";
	
    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        --r_data <= (others => '0');

        -- Reset generation
        -- EDIT: Check that rst_i is really your reset signal
        rst_i <= '1';
        wait for 20 ns;
        rst_i <= '0';
	wait for 1 ns;
	paquete_ok <= '1';
        wait for 10000 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

--    datos : process
--    begin
--        
--        
--        paquete_i <= "101010101010101";
-- 	wait for 8 ns ;
--
--	--paquete_i <= "111111111100001";
-- 	--wait for 200 ns;
--
--	
--
--        --wait for 100 * TbPeriod;
--	--TbSimEnded <= '1';
--    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_fifo_enclavamiento of tb_fifo_enclavamiento is
    for tb
    end for;
end cfg_tb_fifo_enclavamiento;
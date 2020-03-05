-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_registro is
end tb_registro;

architecture tb of tb_registro is

    component registro is
	port(
		clk_i: in std_logic;
        	rst_i: in std_logic;
 	        paquete_ok : in std_logic;
  	        paquete_i: in std_logic_vector(15-1 downto 0);
  	        w_data: out std_logic_vector(8-1 downto 0);
  	        wr_uart : out std_logic  -- "char_disp"
	);
    end component;

    signal clk_i     : std_logic;
    signal rst_i     : std_logic;
    signal paquete_ok     : std_logic;
    signal paquete_i   : std_logic_vector (15-1 downto 0); 
    signal w_data    : std_logic_vector (8-1 downto 0);
    signal wr_uart : std_logic;

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : registro
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              paquete_i   => paquete_i,
              paquete_ok => paquete_ok,
              w_data     => w_data,
 	      wr_uart    => wr_uart);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk_i is really your main clock signal
    clk_i <= TbClock;

    
	
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
	
        wait for 1000000 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        --TbSimEnded <= '1';
        --wait;
    end process;

    datos : process
    begin
        
        
        paquete_i <= "101010101010101";
	paquete_ok <= '1';
 	wait for 1000 * TbPeriod;
	paquete_ok <= '0';
	
	wait for 1000 * TbPeriod;

	paquete_i <= "110110110110110";
 	paquete_ok <= '1';
 	wait for 1000 * TbPeriod;
	paquete_ok <= '0';

	

        --wait for 100 * TbPeriod;
	--TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_registro of tb_registro is
    for tb
    end for;
end cfg_tb_registro;
-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_conector_test is
end tb_conector_test;

architecture tb of tb_conector_test is

    component conector_test
        port(
		clk_i: in std_logic;
        	rst_i: in std_logic;
        	switch : in std_logic;
        	leds : out std_logic_vector(2-1 downto 0);
        	wr_uart_3 : out std_logic;
       	 	N_1 : in integer;
       	 	N_2 : in integer;
        	r_disponible : in std_logic;
        	w_data_1: in std_logic_vector(8-1 downto 0);
        	w_data_2: in std_logic_vector(8-1 downto 0);
        	w_data_3: out std_logic_vector(8-1 downto 0)
	);
    end component;

    signal clk_i,rst_i,switch,wr_uart_3,r_disponible     : std_logic;
    signal leds      : std_logic_vector(2-1 downto 0);
    signal N_1,N_2   : integer;
    signal w_data_1,w_data_2,w_data_3 : std_logic_vector(8-1 downto 0);

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

	 -- Low-level byte-write
  	procedure Enviar_char (
    		data       : in  std_logic_vector(8-1 downto 0);
    		signal r_data : out std_logic_vector(8-1 downto 0);
		signal r_disponible : out std_logic) is
  	begin
		
		r_disponible <= '0';
		wait for TbPeriod;
        	r_data <= data;
		wait for 407 * TbPeriod;
		r_disponible <= '1';
		wait for TbPeriod;
		r_disponible <= '0';

  	end Enviar_char;

begin

    dut : conector_test
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              switch     => switch,
	      leds 	 => leds,
              wr_uart_3  => wr_uart_3,
              N_1  	 => N_1,
              N_2    	 => N_2,
	      r_disponible => r_disponible,
	      w_data_1   => w_data_1,
	      w_data_2   => w_data_2,
	      w_data_3   => w_data_3);
 
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
        wait for 100 ns;
        rst_i <= '0';

	
        wait for 1000000 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

    datos : process
    begin
        
	w_data_2 <= "00000000";
	N_2 <= 0;
	switch <= '0';

	wait for 200 ns;

	-- 21
	N_1 <= 23; 	
	r_disponible <= '1';
	--wait for 5 * TbPeriod;
	Enviar_char("00111100",w_data_1,r_disponible); -- < 	
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110001",w_data_1,r_disponible); -- 1
 	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00110000",w_data_1,r_disponible); -- 0
	Enviar_char("00110000",w_data_1,r_disponible); -- 0	
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 
	Enviar_char("00110001",w_data_1,r_disponible); -- 1 	
	Enviar_char("00111110",w_data_1,r_disponible); -- >
	--wait for 5 * TbPeriod;
	r_disponible <= '0';
	wait for 1000 * TbPeriod;

--	-- 21
--	N <= 23; 	
--	Enviar_char("00111100",r_data,r_disponible); -- < 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1
-- 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110000",r_data,r_disponible); -- 0 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00111110",r_data,r_disponible); -- >
--
--	wait for 100 * TbPeriod;
--
--	-- 22
--	N <= 24; 	
--	Enviar_char("00111100",r_data,r_disponible); -- < 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
-- 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 
--	Enviar_char("00110000",r_data,r_disponible); -- 0	
--	Enviar_char("00111110",r_data,r_disponible); -- >
--	
--	wait for 100 * TbPeriod;
--
--	-- 21
--	N <= 23; 	
--	Enviar_char("00111100",r_data,r_disponible); -- < 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1
-- 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00110000",r_data,r_disponible); -- 0
--	Enviar_char("00110000",r_data,r_disponible); -- 0 	
--	Enviar_char("00110001",r_data,r_disponible); -- 1
--	Enviar_char("00110001",r_data,r_disponible); -- 1 	
--	Enviar_char("00111110",r_data,r_disponible); -- >


        --wait for 100 * TbPeriod;
	--TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_conector_test of tb_conector_test is
    for tb
    end for;
end cfg_tb_conector_test;
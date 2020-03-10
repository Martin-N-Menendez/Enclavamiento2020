-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_sistema is
end tb_sistema;

architecture tb of tb_sistema is

    component sistema
       port(
		clk_i: in std_logic;
        	rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		r_disponible : in std_logic;
		leer : out std_logic;
		escribir : out std_logic;
		switch1 : in std_logic;
		switch2 : in std_logic;
		reset_uart : out std_logic;
		N : in integer;
		--leds : out std_logic_vector(2-1 downto 0);
		leds : out std_logic_vector(4-1 downto 0);
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;


    signal clk_i     : std_logic;
    signal rst_i     : std_logic;
    signal r_data    : std_logic_vector (8-1 downto 0);
    signal r_disponible : std_logic;
    signal leer : std_logic;
    signal escribir : std_logic;
    signal switch1    : std_logic;
    signal switch2   : std_logic;
    signal reset_uart : std_logic;
    signal N : integer;
    signal leds      : std_logic_vector(4-1 downto 0);
    signal led_rgb_1 : std_logic_vector (3-1 downto 0);
    signal led_rgb_2 : std_logic_vector (3-1 downto 0);

    signal w_data    : std_logic_vector (8-1 downto 0);

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
		wait for TbPeriod;
		r_disponible <= '1';
		wait for TbPeriod;
		r_disponible <= '0';

  	end Enviar_char;

begin

    dut : sistema
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              r_data     => r_data,
	      r_disponible => r_disponible,
	      leer       => leer,
 	      escribir   => escribir,
	      switch1    => switch1,
	      switch2    => switch2,
	      reset_uart => reset_uart,
   	      N          => N,
	      leds 	 => leds,
              led_rgb_1  => led_rgb_1,
              led_rgb_2  => led_rgb_2,
              w_data     => w_data);

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
	switch1 <= '1';
	switch2 <= '1';
        wait for 250000 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

    datos : process
    begin
        
	r_data <= "00000000";
	r_disponible <= '0';

	wait for 100 ns;

	-- 21
	N <= 23; 	
	Enviar_char("00111100",r_data,r_disponible); -- < 	
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110001",r_data,r_disponible); -- 1
 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110000",r_data,r_disponible); -- 0 	
	Enviar_char("00110001",r_data,r_disponible); -- 1
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00111110",r_data,r_disponible); -- >

	wait for 100 * TbPeriod;

	-- 21
	N <= 23; 	
	Enviar_char("00111100",r_data,r_disponible); -- < 	
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110001",r_data,r_disponible); -- 1
 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110000",r_data,r_disponible); -- 0 	
	Enviar_char("00110001",r_data,r_disponible); -- 1
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00111110",r_data,r_disponible); -- >

	wait for 100 * TbPeriod;

	-- 22
	N <= 24; 	
	Enviar_char("00111100",r_data,r_disponible); -- < 	
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 
	Enviar_char("00110000",r_data,r_disponible); -- 0	
	Enviar_char("00111110",r_data,r_disponible); -- >
	
	wait for 100 * TbPeriod;

	-- 21
	N <= 23; 	
	Enviar_char("00111100",r_data,r_disponible); -- < 	
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110001",r_data,r_disponible); -- 1
 	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00110000",r_data,r_disponible); -- 0
	Enviar_char("00110000",r_data,r_disponible); -- 0 	
	Enviar_char("00110001",r_data,r_disponible); -- 1
	Enviar_char("00110001",r_data,r_disponible); -- 1 	
	Enviar_char("00111110",r_data,r_disponible); -- >


        wait for 100 * TbPeriod;
	TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

--configuration cfg_tb_sistema of tb_sistema is
--    for tb
--    end for;
--end cfg_tb_sistema;
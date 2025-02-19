-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_detector is
end tb_detector;

architecture tb of tb_detector is

    component detector
        port(
		clk_i: in std_logic;
       		rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		r_disponible : in std_logic;
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		paquete: out std_logic_vector(21-1 downto 0);
		procesar : in std_logic;
		procesado : out std_logic;
		N : in integer;
		N_1 : out integer;
		N_2 : out integer;
		wr_uart : out std_logic;
		w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;

    signal clk_i     : std_logic;
    signal rst_i     : std_logic;
    signal r_data    : std_logic_vector (8-1 downto 0);
    signal r_disponible      : std_logic;
    signal led_rgb_1 : std_logic_vector (3-1 downto 0);
    signal led_rgb_2 : std_logic_vector (3-1 downto 0);
    signal paquete   : std_logic_vector (21-1 downto 0); 
    signal procesar : std_logic;
    signal procesado : std_logic;
    signal N,N_1,N_2 : integer;
    signal wr_uart : std_logic;
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

    dut : detector
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              r_data     => r_data,
	      r_disponible => r_disponible,
              led_rgb_1  => led_rgb_1,
              led_rgb_2  => led_rgb_2,
              paquete    => paquete,
	      procesar   => procesar,
      	      procesado  => procesado,
	      N 	 => N,
              N_1        => N_1,
 	      N_2 	 => N_2,
	      wr_uart    => wr_uart,
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
	--r_data <= "00000000";
	--r_disponible <= '0';
        wait for 100 ns;
        rst_i <= '0';

	
        wait for 1000 * TbPeriod;

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

--configuration cfg_tb_detector of tb_detector is
--    for tb
--    end for;
--end cfg_tb_detector;
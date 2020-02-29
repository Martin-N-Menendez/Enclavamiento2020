-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;

entity tb_uart_loop is
end tb_uart_loop;

architecture tb of tb_uart_loop is

    component uart_loop
        port(
		clk_i: in std_logic;
		rst_i: in std_logic;
		uart_rxd_i: in std_logic;
		uart_txd_o: out std_logic;
		leds  : out std_logic_vector(4-1 downto 0);
		rgb_1  : out std_logic_vector(3-1 downto 0);
		rgb_2  : out std_logic_vector(3-1 downto 0);
		--empty_o: out std_logic;
		--full_o: out std_logic;
		switch1 : in std_logic;
		switch2 : in std_logic
	);
    end component;


    signal clk_i     	 : std_logic;
    signal rst_i     	 : std_logic;
    signal uart_rxd_i    : std_logic;
    signal uart_txd_o    : std_logic;
    signal leds      	 : std_logic_vector(4-1 downto 0);
    signal rgb_1   	 : std_logic_vector (3-1 downto 0);
    signal rgb_2 	 : std_logic_vector (3-1 downto 0);
    signal switch1	 : std_logic;
    signal switch2	 : std_logic;
    --signal full_o	 : std_logic;

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

    -- 1/19200:
    constant c_BIT_PERIOD : time := 407 * TbPeriod;

	 -- Low-level byte-write
  	procedure UART_WRITE_BYTE (
    		i_Data_In       : in  std_logic_vector(7 downto 0);
    		signal o_Serial : out std_logic) is
  	begin

   		-- Send Start Bit
    		o_Serial <= '0';
    		wait for c_BIT_PERIOD;

    		-- Send Data Byte
    		for ii in 0 to 7 loop
      			o_Serial <= i_Data_In(ii);
     			wait for c_BIT_PERIOD;
    		end loop;  -- ii

    		-- Send Stop Bit
    		o_Serial <= '1';
    		wait for c_BIT_PERIOD;
  	end UART_WRITE_BYTE;

begin

    dut : uart_loop
    port map (clk_i      => clk_i,
              rst_i      => rst_i,
              uart_rxd_i => uart_rxd_i,
	      uart_txd_o => uart_txd_o,
	      leds 	 => leds,
              rgb_1 	 => rgb_1,
              rgb_2  	 => rgb_2,
	      --empty_o 	 => empty_o,
	      switch1	 => switch1,
	      switch2	 => switch2
    	      --full_o	 => full_o
              );

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
	switch1 <= '0';
	switch2 <= '0';
        wait for 1000 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

    datos : process
    begin
        
	wait for 200 ns;
	--21
	UART_WRITE_BYTE(X"3C", uart_rxd_i);

	wait for 200 ns;
	
--	wait for 100 ns;
--	-- 21
--        r_data <= "00111100"; -- <
-- 	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00111110"; -- >
--
--	wait for 100 ns;
--	-- 22
--        r_data <= "00111100"; -- <
-- 	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00111110"; -- >
--	
--	wait for 100 ns;
--	-- 23
--        r_data <= "00111100"; -- <
-- 	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00110000"; -- 0
--	wait for 50 ns;
--	r_data <= "00110001"; -- 1
--	wait for 50 ns;
--	r_data <= "00111110"; -- >

        wait for 10000 * TbPeriod;
	TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_uart_loop of tb_uart_loop is
    for tb
    end for;
end cfg_tb_uart_loop;
-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;

entity tb_cambio is
end tb_cambio;

architecture tb of tb_cambio is

    component cambio_1 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_ante_i :  in std_logic;
			Estado_post_i :  in std_logic;
			Estado_desv_i :  in std_logic;
			Estado_ante_o :  out std_logic;
			Estado_post_o :  out std_logic;
			Estado_desv_o :  out std_logic;
			Cambio_i :  in std_logic;
			Cambio_o :  out std_logic
		);
    end component;

    Signal Clock : std_logic;
	Signal Reset : std_logic;
	Signal Estado_ante_i :  std_logic;
	Signal Estado_post_i : std_logic;
	Signal Estado_desv_i :  std_logic;
	Signal Estado_ante_o : std_logic;
	Signal Estado_post_o :  std_logic;
	Signal Estado_desv_o : std_logic;
	Signal Cambio_i :  std_logic;
	Signal Cambio_o : std_logic;

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut :  cambio_1
    port map (
			  Clock           => Clock,
              Reset           => Reset,
			  Estado_ante_i   => Estado_ante_i,
			  Estado_post_i   => Estado_post_i,
			  Estado_desv_i   => Estado_desv_i,
			  Estado_ante_o   => Estado_ante_o,
			  Estado_post_o   => Estado_post_o,
			  Estado_desv_o   => Estado_desv_o,
			  Cambio_i        => Cambio_i,
			  Cambio_o        => Cambio_o
			  );

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk_i is really your main clock signal
    Clock <= TbClock;

    -- (cambio_i,estado_ante_i,estado_post_i,estado_desv_i)
	-- (0,0,0,0):
	-- (0,0,0,1):
	-- (0,0,1,0):
	-- (0,0,1,1):
	-- (0,1,0,0):
	-- (0,1,0,1):
	-- (0,1,1,0):
	-- (0,1,1,1):
	-- (1,0,0,0):
	-- (1,0,0,1):
	-- (1,0,1,0):
	-- (1,0,1,1):
	-- (1,1,0,0):
	-- (1,1,0,1):
	-- (1,1,1,0):
	-- (1,1,1,1):
    datos : process
    begin
        Reset <= '0';
		wait for 1 * TbPeriod;
		Reset <= '1';
		
		-- (0,0,0,0):
		Cambio_i <= '0';
		Estado_ante_i <= '0';
		Estado_post_i <= '0';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (0,0,0,1):
		Cambio_i <= '0';
		Estado_ante_i <= '0';
		Estado_post_i <= '0';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		-- (0,0,1,0):
		Cambio_i <= '0';
		Estado_ante_i <= '0';
		Estado_post_i <= '1';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (0,0,1,1):
		Cambio_i <= '0';
		Estado_ante_i <= '0';
		Estado_post_i <= '1';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		-- (0,1,0,0):
		Cambio_i <= '0';
		Estado_ante_i <= '1';
		Estado_post_i <= '0';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (0,1,0,1):
		Cambio_i <= '0';
		Estado_ante_i <= '1';
		Estado_post_i <= '0';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		-- (0,1,1,0):
		Cambio_i <= '0';
		Estado_ante_i <= '1';
		Estado_post_i <= '1';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (0,1,1,1):
		Cambio_i <= '0';
		Estado_ante_i <= '1';
		Estado_post_i <= '1';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;		
		-- (1,0,0,0):
		Cambio_i <= '1';
		Estado_ante_i <= '0';
		Estado_post_i <= '0';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (1,0,0,1):
		Cambio_i <= '1';
		Estado_ante_i <= '0';
		Estado_post_i <= '0';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		-- (1,0,1,0):
		Cambio_i <= '1';
		Estado_ante_i <= '0';
		Estado_post_i <= '1';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (1,0,1,1):
		Cambio_i <= '1';
		Estado_ante_i <= '0';
		Estado_post_i <= '1';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		-- (1,1,0,0):
		Cambio_i <= '1';
		Estado_ante_i <= '1';
		Estado_post_i <= '0';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (1,1,0,1):
		Cambio_i <= '1';
		Estado_ante_i <= '1';
		Estado_post_i <= '0';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		-- (1,1,1,0):
		Cambio_i <= '1';
		Estado_ante_i <= '1';
		Estado_post_i <= '1';
		Estado_desv_i <= '0';
		wait for 20 * TbPeriod;
		-- (1,1,1,1):
		Cambio_i <= '1';
		Estado_ante_i <= '1';
		Estado_post_i <= '1';
		Estado_desv_i <= '1';
		wait for 20 * TbPeriod;
		
        wait for 500 * TbPeriod;
	--TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_cambio of tb_cambio is
    for tb
    end for;
end cfg_tb_cambio;
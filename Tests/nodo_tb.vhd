-- Testbench automatically generated online
-- at http://vhdl.lapinoo.net
-- Generation date : 11.2.2020 22:32:39 GMT

library ieee;
use ieee.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;

entity tb_nodo is
end tb_nodo;

architecture tb of tb_nodo is

    component nodo_1 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_post :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Semaforo_lejano :  out sem_type;
			Estado_o :  out std_logic
		);
    end component;

    Signal Clock : std_logic;
	Signal Reset : std_logic;
	Signal Estado_i :  std_logic;
	Signal Estado_post : std_logic;
	Signal Semaforo_propio_i_1 : sem_type;
	Signal Semaforo_propio_o_1 : sem_type;
	Signal Semaforo_cercano :  sem_type;
	Signal Semaforo_lejano :  sem_type;
	Signal Estado_o :  std_logic;

    constant TbPeriod : time := 8 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut :  nodo_1
    port map (
			  Clock      => Clock,
              Reset      => Reset,
			  Estado_i   => Estado_i,
			  Estado_post => Estado_post,
			  Semaforo_propio_i_1 => Semaforo_propio_i_1,
			  Semaforo_propio_o_1 => Semaforo_propio_o_1,
			  Semaforo_cercano => Semaforo_cercano,
			  Semaforo_lejano => Semaforo_lejano,
			  Estado_o => Estado_o
			  );

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk_i is really your main clock signal
    Clock <= TbClock;

    -- (Yo,Vecino,Aspecto vecino)
	-- (0,0,0,0):
	-- (0,0,0,1):
	-- (0,0,1,1):
	-- (0,1,0,0):
	-- (0,1,0,1):
	-- (0,1,1,1):
	-- (1,0,0,0):
	-- (1,0,0,1):
	-- (1,0,1,1):
	-- (1,1,0,0):
	-- (1,1,0,1):
	-- (1,1,1,1):
    datos : process
    begin
        Reset <= '0';
		wait for 1 * TbPeriod;
		Reset <= '1';
		
		-- (0,0,0,0):
		Estado_i <= '0';
		Estado_post <= '0';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '0';
		wait for 20 * TbPeriod;
		-- (0,0,0,1):
		Estado_i <= '0';
		Estado_post <= '0';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (0,0,1,1):
		Estado_i <= '0';
		Estado_post <= '0';
		Semaforo_propio_i_1.lsb <= '1';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (0,1,0,0):
		Estado_i <= '0';
		Estado_post <= '1';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '0';
		wait for 20 * TbPeriod;
		-- (0,1,0,1):
		Estado_i <= '0';
		Estado_post <= '1';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (0,1,1,1):
		Estado_i <= '0';
		Estado_post <= '1';
		Semaforo_propio_i_1.lsb <= '1';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (1,0,0,0):
		Estado_i <= '1';
		Estado_post <= '0';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '0';
		wait for 20 * TbPeriod;
		-- (1,0,0,1):
		Estado_i <= '1';
		Estado_post <= '0';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (1,0,1,1):
		Estado_i <= '1';
		Estado_post <= '0';
		Semaforo_propio_i_1.lsb <= '1';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (1,1,0,0):
		Estado_i <= '1';
		Estado_post <= '1';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '0';
		wait for 20 * TbPeriod;
		-- (1,1,0,1):
		Estado_i <= '1';
		Estado_post <= '1';
		Semaforo_propio_i_1.lsb <= '0';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		-- (1,1,1,1):
		Estado_i <= '1';
		Estado_post <= '1';
		Semaforo_propio_i_1.lsb <= '1';
		Semaforo_propio_i_1.msb <= '1';
		wait for 20 * TbPeriod;
		
        wait for 500 * TbPeriod;
	--TbSimEnded <= '1';
    end process;
	
end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_nodo of tb_nodo is
    for tb
    end for;
end cfg_tb_nodo;
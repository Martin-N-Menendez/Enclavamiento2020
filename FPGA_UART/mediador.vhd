-- mediador.vhdl : Achivo VHDL generado automaticamente

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

--Declare the package

use work.my_package.all;
	
	entity mediador is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			procesar :  in std_logic;
			procesado :  out std_logic;
			semaforos :  in sems_type;
			Cambios :  in std_logic;
			Salida :  out std_logic_vector(15-1 downto 0);
			Reset :  in std_logic
		);
	end entity mediador;
	
architecture Behavioral of mediador is

begin

	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Salida <= (others => '0'); 
				procesado <= '0';
			else
			    procesado <= procesar;
			    if (procesar = '1') then
                    Salida(0) <= semaforos.msb(0);
                    Salida(1) <= semaforos.lsb(0);
                    Salida(2) <= semaforos.msb(1);
                    Salida(3) <= semaforos.lsb(1);
                    Salida(4) <= semaforos.msb(2);
                    Salida(5) <= semaforos.lsb(2);
                    Salida(6) <= semaforos.msb(3);
                    Salida(7) <= semaforos.lsb(3);
                    Salida(8) <= semaforos.msb(4);
                    Salida(9) <= semaforos.lsb(4);
                    Salida(10) <= semaforos.msb(5);
                    Salida(11) <= semaforos.lsb(5);
                    Salida(12) <= semaforos.msb(6);
                    Salida(13) <= semaforos.lsb(6);
                    Salida(14) <= Cambios;
                end if;    
			end if;
		end if;
	end process;
	
end Behavioral;


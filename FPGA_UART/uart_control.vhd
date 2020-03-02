library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity uart_control is
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
end uart_control;

architecture Behavioral of uart_control is

signal emptySignal: std_logic;
    
begin
    process(clk_i)
        variable count: integer := 0;
        variable L : integer := 0;
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                L := 0;
            else 
                if empty_o = '0' then   -- Tiene datos  
                             
                --if leer = '1' then
                    rd_uart <= '1';     -- Pido el dato
                    wr_uart <= '1';
                    L := L + 1;
                --else                    
                    --rd_uart <= '0';

                --end if;                             
                else                    -- No tiene datos
                    N <= L;
                    rd_uart <= '0';
                    wr_uart <= '0';
       
                end if;
            end if;
        end if;
     
    end process;
    
   
--    process(clk_i)
--        variable cosa: integer := 0;
--        --variable L : integer := 0;
--    begin
--        if (clk_i = '1' and clk_i'event) then
--            if rst_i = '1' then          
--                cosa := 0; 
--            elsif full_o = '0' then   -- Tiene espacio
--                --count := count + 1;
                             
--                --if count = 125E4 then    -- Cuento 10 mseg
--                if escribir = '1' then
--                    wr_uart <= '1';
--                else                    
--                    wr_uart <= '0';
--                end if;
                                
--            else                    -- No tiene espacio
--                wr_uart <= '0';
--            end if;
--        end if;
     
--    end process;
    
end Behavioral;

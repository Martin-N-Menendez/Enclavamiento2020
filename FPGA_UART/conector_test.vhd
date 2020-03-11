library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity conector_test is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        switch : in std_logic;
        leds : out std_logic_vector(2-1 downto 0);
        wr_uart_3 : out std_logic;
        wr_uart_1 : in std_logic;
        wr_uart_2 : in std_logic;
        w_data_1: in std_logic_vector(8-1 downto 0);
        w_data_2: in std_logic_vector(8-1 downto 0);
        w_data_3: out std_logic_vector(8-1 downto 0)
	);
    end entity;

architecture Behavioral of conector_test is
  
  signal disp_aux : std_logic_vector(8-1 downto 0);
    
begin
     
    process(clk_i)
    variable contador: integer := 0;
    variable N_total : integer := 0;
    
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                N_total := 0; 
                contador := 0; 
                w_data_3 <= "00000000";
                wr_uart_3 <= '0';
            else 
                if switch = '1' then                 
                    
                    disp_aux <= w_data_2;
                    
                    w_data_3 <= disp_aux;
                                 
                    wr_uart_3 <= wr_uart_2;
                              
                    --leds <= "10";
                else   
       
                    disp_aux <= w_data_1;
                    
                    w_data_3 <= disp_aux;
                                 
                    wr_uart_3 <= wr_uart_1;
                        
     
                                       
      
                    --leds <= "01";
                end if;
            end if;
        end if;
    end process;  
    
        
end Behavioral;
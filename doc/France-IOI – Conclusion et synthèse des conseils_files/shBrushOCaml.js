/**
 * SyntaxHighlighter
 * http://alexgorbatchev.com/SyntaxHighlighter
 *
 * SyntaxHighlighter is donationware. If you are using it, please donate.
 * http://alexgorbatchev.com/SyntaxHighlighter/donate.html
 *
 * @version
 * 3.0.83 (July 02 2010)
 * 
 * @copyright
 * Copyright (C) 2004-2010 Alex Gorbatchev.
 *
 * @license
 * Dual licensed under the MIT and GPL licenses.
 */
;(function()
{
	// CommonJS
	typeof(require) != 'undefined' ? SyntaxHighlighter = require('shCore').SyntaxHighlighter : null;

	function Brush()
	{
		// Copyright 2006 Shin, YoungJin
	
		var datatypes =	'array bool char exn file_descr format fpclass ' +
                        'in_channel int int32 int64 list nativeint open_flag '+
                        'out_channel string Sys_error unit';
                        
		var keywords =	'and as asr begin class closed constraint do done downto else ' +
                        'end exception external failwith false for fun function functor ' +
                        'if in include inherit  incr land let load los lsl lsr lxor ' +
                        'match method mod module mutable new not of open option or parser ' +
                        'private ref rec raise regexp sig struct stdout stdin stderr then ' +
                        'to true try type val virtual when while with';
                        
        var libraries = 'Arg  Arith_status  Array ArrayLabels  Big_int  Bigarray ' +
                        'Buffer  Callback CamlinternalLazy  CamlinternalMod  CamlinternalOO ' +
                        'Char Complex  Condition  Dbm  Digest  Dynlink  Event ' +
                        'Filename  Format  Gc  Genlex  Graphics  GraphicsX11 ' +
                        'Hashtbl  Int32  Int64  Lazy  Lexing  List  ListLabels ' +
                        'Map  Marshal  MoreLabels  Mutex  Nativeint  Num  Obj ' +
                        'Oo  Parsing  Pervasives  Printexc  Printf  Queue ' +
                        'Random  Scanf  Set  Sort  Stack  StdLabels  Str ' +
                        'Stream  String  StringLabels  Sys  Thread  ThreadUnix ' +
                        'Tk  Unix  UnixLabels  Weak';
                        
		var functions =	'abs  abs_float  acos  asin  at_exit  atan  atan2 ' +
                        'bool_of_string  ceil  char_of_int  classify_float ' +
                        'close_in  close_in_noerr  close_out  close_out_noerr ' +
                        'compare  cos  cosh  decr  epsilon_float  exit  exp ' +
                        'float  float_of_int  float_of_string  floor  flush ' +
                        'flush_all  format_of_string  frexp  fst  ignore ' +
                        'in_channel_length  infinity  input  input_binary_int ' +
                        'input_byte  input_char  input_line  input_value ' +
                        'int_of_char  int_of_float  int_of_string  invalid_arg ' +
                        'ldexp  log  log10  max  max_float  max_int  min ' +
                        'min_float  min_int  mod_float  modf  nan  open_in ' +
                        'open_in_bin  open_in_gen  open_out  open_out_bin ' +
                        'open_out_gen  out_channel_length  output  output_binary_int ' +
                        'output_byte  output_char  output_string  output_value ' +
                        'pos_in  pos_out   pred  prerr_char  prerr_endline ' +
                        'prerr_float  prerr_int  prerr_newline  prerr_string ' +
                        'print_char  print_endline  print_float  print_int ' +
                        'print_newline  print_string  read_float  read_int ' +
                        'read_line  really_input  seek_in  seek_out ' +
                        'set_binary_mode_in  set_binary_mode_out  sin  sinh  snd ' +
                        'sqrt  string_of_bool  string_of_float  string_of_format ' +
                        'string_of_int  succ  tan  tanh  truncate';
        var exceptions = 'Exit  Invalid_Argument  Failure  Division_by_zero';

		this.regexList = [
			{ regex: /\(\*(.|\n|\r)*?\*\)/gi,	                        css: 'comments' },			// comments
			{ regex: SyntaxHighlighter.regexLib.doubleQuotedString,		css: 'string' },			// strings
            { regex: /\b([\d]+(\.[\d]+)?|0x[a-f0-9]+)\b/gi,				css: 'value' },
			{ regex: /^ *#.*/gm,										css: 'preprocessor' },
			{ regex: new RegExp(this.getKeywords(datatypes), 'gm'),		css: 'color1 bold' },
			{ regex: new RegExp(this.getKeywords(libraries), 'gm'),		css: 'color2 bold' }, 
			{ regex: new RegExp(this.getKeywords(exceptions), 'gm'),	css: 'color3 bold' },
			{ regex: new RegExp(this.getKeywords(functions), 'gm'),		css: 'functions bold' },
			{ regex: new RegExp(this.getKeywords(keywords), 'gm'),		css: 'keyword bold' }
			];
	};
    /*
plain
    comments
    string
    keyword
preprocessor
variable
    value
    functions
constants
color1
color2
color3   

//symbols
*/
	Brush.prototype	= new SyntaxHighlighter.Highlighter();
	Brush.aliases	= ['OCaml', 'ocaml'];

	SyntaxHighlighter.brushes.OCaml = Brush;

	// CommonJS
	typeof(exports) != 'undefined' ? exports.Brush = Brush : null;
})();

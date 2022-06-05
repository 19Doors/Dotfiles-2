/* See LICENSE file for copyright and license details. */
/* Default settings; can be overriden by command line. */

static int topbar = 1;                      /* -b  option; if 0, dmenu appears at bottom     */
/* -fn option overrides fonts[0]; default X11 font or font set */
static const char *fonts[] = {
	"Iosevka Nerd Font:size=14"
};
static const char *prompt      = NULL;      /* -p  option; prompt to the left of input field */
static const char *colors[SchemeLast][2] = {
	/*     fg         bg       */
	[SchemeNorm] = { "#F1EDEE", "#010206" },
	[SchemeSel] = { "#F1EDEE", "#5FA8D3" },
	//[SchemeOut] = { "#F1EDEE", "#010206" },
	[SchemeOut] = { "#F1EDEE", "#F1EDEE" },
	[SchemeSelHighlight] = { "#F1EDEE", "#5FA8D3" },
	[SchemeNormHighlight] = { "#CE6A85", "#010206" },
};
/* -l option; if nonzero, dmenu uses vertical list with given number of lines */
static unsigned int lines = 10;

/*
 * Characters not considered part of a word while deleting words
 * for example: " /?\"&[]"
 */
static const char worddelimiters[] = " ";
static const unsigned int border_width = 5;

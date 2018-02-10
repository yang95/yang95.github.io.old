﻿/*********************************************************************NVMH3****
File:  $Id: //sw/devtools/SDK/9.5/SDK/MEDIA/HLSL/paint_brush.fx#3 $

Copyright NVIDIA Corporation 2002-2004
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, THIS SOFTWARE IS PROVIDED
*AS IS* AND NVIDIA AND ITS SUPPLIERS DISCLAIM ALL WARRANTIES, EITHER EXPRESS
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE.  IN NO EVENT SHALL NVIDIA OR ITS SUPPLIERS
BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT, OR CONSEQUENTIAL DAMAGES
WHATSOEVER (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF BUSINESS PROFITS,
BUSINESS INTERRUPTION, LOSS OF BUSINESS INFORMATION, OR ANY OTHER PECUNIARY LOSS)
ARISING OUT OF THE USE OF OR INABILITY TO USE THIS SOFTWARE, EVEN IF NVIDIA HAS
BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.


Comments:
	An .FX Paint Program. Scene geometry is ignored.
	Draw with the left mouse button.
	To clear screen, just make the brush big and paint everything.
	Resizing the window will mess up your drawing.
	Brush strokes will change in size and opacity over time, set "FadeTime"
		to a high value for more even (though less expressive) strokes.

******************************************************************************/

#include <Quad.fxh>

float Script : STANDARDSGLOBAL
<
	string UIWidget = "none";
	string ScriptClass = "scene";
	string ScriptOrder = "standard";
	string ScriptOutput = "color";
	// We just call a script in the main technique.
	string Script = "Technique=paint;";
> = 0.8; // version #

bool bReset : FXCOMPOSER_RESETPULSE
<
	string UIName="Clear Canvas";
>;

bool bRevert
<
	string UIName="Use BgPic instead of BgColor?";
> = true;

float4 BgColor <
	string UIWidget = "color";
	string UIName = "Background";
> = {1.0,0.95,0.92,1.0};

float ClearDepth <string UIWidget = "none";> = 1.0;

///////////// untweakables //////////////////////////

float4 MouseL : LEFTMOUSEDOWN < string UIWidget="None"; >;
float3 MousePos : MOUSEPOSITION < string UIWidget="None"; >;
float Timer : TIME < string UIWidget = "None"; >;

////////////// tweakables /////////////////////////

float Opacity <
	string UIWidget = "slider";
	float UIMin = 0.0;
	float UIMax = 1.0;
	float UIStep = 0.01;
> = 0.5f;

float BrushSizeStart <
	string UIWidget = "slider";
	float UIMin = 0.001;
	float UIMax = 0.15;
	float UIStep = 0.001;
> = 0.07f;

float BrushSizeEnd <
	string UIWidget = "slider";
	float UIMin = 0.001;
	float UIMax = 0.15;
	float UIStep = 0.001;
> = 0.07f;

float FadeTime <
	string UIWidget = "slider";
	float UIMin = 0.1;
	float UIMax = 10.0;
	float UIStep = 0.1;
> = 2.00f;

float3 PaintColor <
	string UIWidget = "Color";
> = {0.4f, 0.3f, 1.0f};



float lerpsize()
{
	//float f = fadeout();
	//float ds = lerp(BrushSizeEnd,BrushSizeStart,f);
	return BrushSizeStart;
}

FILE_TEXTURE_2D_MODAL(BgPic,BgSampler,"default_color.dds",CLAMP)
FILE_TEXTURE_2D_MODAL(FgPic,FgSampler,"floor.png",CLAMP)

texture PaintTex : RENDERCOLORTARGET 
<
	float2 Dimensions = { 512, 512 }; 
    string Format = "a8b8g8r8";
	string UIWidget = "None";
	int MipLevels = 1;
>;

sampler PaintSamp = sampler_state 
{
    texture = <PaintTex>;
    AddressU  = CLAMP;
    AddressV  = CLAMP;
    MipFilter = None;
    MinFilter = POINT;
    MagFilter = POINT;
};

texture DepthStencilTarget : RENDERDEPTHSTENCILTARGET
<
	float2 Dimensions = { 512, 512 }; 
	string format = "D24S8";
    string UIWidget = "None";
>;


/***************************************************/
/*** This shader performs the clear/revert *********/
/***************************************************/

float4 revertPS(QuadVertexOutput IN,uniform float UseTex) : COLOR
{
    return float4(0,0,0,0);
}

/***************************************************/
/*** The dead-simple paintbrush shader *************/
/***************************************************/
float4 reducePS(QuadVertexOutput IN
	) : COLOR
{
    
    float4 cur = tex2D(PaintSamp,IN.UV.xy);
    cur = cur - 0.003f;
    if(cur.x<0.001)  cur = float4(0,0,0,0);
    return cur;
}
float4 strokePS(QuadVertexOutput IN) : COLOR
{
     
    
    float2 delta = IN.UV.xy-MousePos.xy;
    //if(length(delta)<0.05) delta = float2(0,0);
    float dd = (1-min((length(delta)-0.01)/BrushSizeStart,1));  //°뾶
    dd *= Opacity*MousePos.z ;    
    return float4(1,1,1,dd);
}

float4 strokePS2(QuadVertexOutput IN) : COLOR
{

    float dd = tex2D(PaintSamp,IN.UV.xy).x;
    return float4(tex2D(FgSampler,IN.UV.xy).xyz,dd);
}



////////////////// Technique ////////

technique paint <
	string Script =
	        "RenderColorTarget0=PaintTex;"
	        "RenderDepthStencilTarget=DepthStencilTarget;"
    		"LoopByCount=bReset;"
				"Pass=;"
    		"LoopEnd=;"
    		"Pass=background;"
        	"Pass=splat;"
        	"Pass=display;"
        	"Pass=dispear;"
        	;
> {
	pass revert <
		string Script = "Draw=Buffer;";
	> {
		VertexShader = compile vs_1_1 ScreenQuadVS();
		//PixelShader  = compile ps_2_0 revertPS((bRevert!=false)?1.0:0.0);
		PixelShader  = compile ps_2_0 revertPS(true);
		AlphaBlendEnable = false;
		ZEnable = false;
	}
	
	pass background <
		string Script = 
		"RenderColorTarget0=;"
		"RenderDepthStencilTarget=;"
		"Draw=Buffer;";
	> {
		VertexShader = compile vs_1_1 ScreenQuadVS();
		PixelShader  = compile ps_2_0 TexQuadPS(BgSampler); //float4 h_curr = tex2D(currentHeightTex, IN.UV.xy);
		AlphaBlendEnable = true;
		SrcBlend = SrcAlpha;
		DestBlend = InvSrcAlpha;
		ZEnable = false;
	} 
	
	pass splat <
		string Script = 
		"RenderColorTarget0=PaintTex;"
		"RenderDepthStencilTarget=DepthStencilTarget;"
		"Draw=Buffer;";
	> {
		VertexShader = compile vs_1_1 ScreenQuadVS();
		PixelShader  = compile ps_2_0 strokePS();
		AlphaBlendEnable = true;
		SrcBlend = SrcAlpha;
		DestBlend = InvSrcAlpha;
		ZEnable = false;
	} 
	
	pass display <
		string Script = 
		"RenderColorTarget0=;"
		"RenderDepthStencilTarget=;"
		"Draw=Buffer;";
	> {
		VertexShader = compile vs_1_1 ScreenQuadVS();
		PixelShader  = compile ps_2_0 strokePS2();
		AlphaBlendEnable = true;
		SrcBlend = SrcAlpha;
		DestBlend = InvSrcAlpha;
		ZEnable = false;
	} 
	
		
	pass dispear <
		string Script = 
		"RenderColorTarget0=PaintTex;"
		"RenderDepthStencilTarget=DepthStencilTarget;"
		"Draw=Buffer;";
	> {
		VertexShader = compile vs_1_1 ScreenQuadVS();
		PixelShader  = compile ps_2_0 reducePS();
		AlphaBlendEnable = false;
		ZEnable = false;
	} 
	
}


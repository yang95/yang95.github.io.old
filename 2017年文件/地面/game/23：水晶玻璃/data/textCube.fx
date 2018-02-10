string description = "Basic Vertex Lighting with a Texture";

//------------------------------------

float4x4 viewProjection : ViewProjection;

float4x4 world : WORLD;


texture diffuseTexture : Diffuse
<
	string ResourceName = "default_color.dds";
>;



//------------------------------------
struct vertexInput {
    float3 position				: POSITION;
    float3 normal				: NORMAL;
    float2 texCoordDiffuse		: TEXCOORD0;
	float4 vInstanceMatrix1 	: TEXCOORD1;
	float4 vInstanceMatrix2	 	: TEXCOORD2;
	float4 vInstanceMatrix3		: TEXCOORD3;
	float4 MapUVarea			: TEXCOORD4;
};

struct vertexOutput {
    float4 hPosition		: POSITION;
    float4 texCoordDiffuse	: TEXCOORD0;
    float4 MapUV			: TEXCOORD1;
    

	
};

float3 line_plane_intercept(float3 lineP,
                            float3 lineN,
                            float3 planeN,
                            float  planeD)
{
  
 float distance = (planeD - dot(planeN,lineP))/dot(lineN, planeN);
  
  return lineP + lineN * distance;
}

//------------------------------------
vertexOutput VS_TransformAndTexture(vertexInput IN) 
{
    vertexOutput OUT = (vertexOutput)0;
    
    
   	float4 row1 = float4(IN.vInstanceMatrix1.x,IN.vInstanceMatrix2.x,IN.vInstanceMatrix3.x,0);
	float4 row2 = float4(IN.vInstanceMatrix1.y,IN.vInstanceMatrix2.y,IN.vInstanceMatrix3.y,0);
	float4 row3 = float4(IN.vInstanceMatrix1.z,IN.vInstanceMatrix2.z,IN.vInstanceMatrix3.z,0);
	float4 row4 = float4(IN.vInstanceMatrix1.w,IN.vInstanceMatrix2.w,IN.vInstanceMatrix3.w,1);
	float4x4 World2 = float4x4(row1,row2,row3,row4);
    
    
    //World2 =  world  ;

    float4 Pos = mul(float4(IN.position,1),World2);   
    Pos = mul(Pos,viewProjection);
    OUT.hPosition  = Pos;         
     
    OUT.texCoordDiffuse = Pos;    
    float4 newNormal = mul( float4(IN.normal,1) , World2);
    newNormal = mul(newNormal,viewProjection);
    
    float3 tranferUV = line_plane_intercept(float3(0,0,0),newNormal,float3(0,0,1),0.5	);
    
    
  // Pos.x=0.1;
   // Pos.y=0.5;
    //return 1;
  	float2 xyBase=0;
  	xyBase.x =Pos.x/12;
  	xyBase.y =Pos.y/9;
  
  
  	float2 mapuv =  (tranferUV.xy*0.05f+0.5f+xyBase);
  	//mapuv.x = mapuv.x * xyBaseArea.x;
  	//mapuv = xyBase;
  	mapuv.y = 1-mapuv.y;
  
    OUT.MapUV = float4(mapuv,1,1);
    
    return OUT;
}


//------------------------------------
sampler TextureSampler = sampler_state 
{
    texture = <diffuseTexture>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};


//-----------------------------------
float4 PS_Textured( vertexOutput IN): COLOR
{

  float4 diffuseTexture = tex2D( TextureSampler,IN.MapUV.xy );
  return diffuseTexture;
}


//-----------------------------------
technique textured
{
    pass p0 
    {		
		VertexShader = compile vs_2_0 VS_TransformAndTexture();
		PixelShader  = compile ps_2_0 PS_Textured();
    }
}